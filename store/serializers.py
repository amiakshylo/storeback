from store.signals import order_crated
from rest_framework import serializers
from decimal import Decimal
from django.db import transaction
from store.models import (
    Address,
    Cart,
    CartItem,
    Customer,
    Order,
    OrderItem,
    Product,
    Collection,
    ProductImage,
    Review,
    FavoriteProduct, ProductRanking, ProductView,
)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return ProductImage.objects.create(product_id=product_id, **validated_data)


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "product_id", "user", "date", "description"]

    def create(self, validated_data):
        product_id = self.context["product_id"]
        user = self.context["username"]
        return Review.objects.create(product_id=product_id, user=user, **validated_data)


class ProductRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRanking
        fields = ['ranking']

    def create(self, validated_data):
        product_id = self.context['product_id']
        user_id = self.context['user_id']
        if ProductRanking.objects.filter(product_id=product_id, user_id=user_id).exists():
            raise serializers.ValidationError('You have already ranked this product')
        return ProductRanking.objects.create(product_id=product_id, user_id=user_id, **validated_data)


class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = ['id', 'timestamp']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    reviews = serializers.IntegerField(read_only=True, source='reviews_count')
    likes = serializers.IntegerField(read_only=True, source='likes_count')
    average_ranking = serializers.IntegerField(read_only=True, source='ranking')
    views = serializers.SerializerMethodField(method_name='get_views_count')

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "inventory",
            "price",
            "price_with_tax",
            "collection",
            "reviews",
            "images",
            "likes",
            "average_ranking",
            "views"
        ]

    def calculate_tax(self, product: Product):
        tax_value = product.unit_price * Decimal(1.1)
        rounded_tax = round(tax_value, 2)
        return rounded_tax

    def get_views_count(self, product: Product):
        return ProductView.objects.filter(product=product).count()


class AddFavoriteProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = FavoriteProduct
        fields = ["id", "product", "user"]


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "unit_price"]


class FavoriteProductSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)

    class Meta:
        model = FavoriteProduct
        fields = ["id", "product"]


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "total_price"]

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='uuid', read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, cart: Cart):
        return sum(
            [item.quantity * item.product.unit_price for item in cart.items.all()]
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "street", "city"]

    def create(self, validated_data):
        customer_id = self.context["customer_id"]
        return Address.objects.create(customer_id=customer_id, **validated_data)


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "user_id", "phone", "birth_date", "membership", "address"]


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["payment_status"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer", "items", "payment_status", "placed_at"]


class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("Cart id does not exist")
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError("The cart is empty")
        return cart_id

    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data["cart_id"]
            customer = Customer.objects.get(user_id=self.context["user_id"])
            order = Order.objects.create(customer=customer)
            cart_items = CartItem.objects.select_related("product").filter(
                cart_id=cart_id
            )
            order_items = [
                OrderItem(order=order, product=item.product, quantity=item.quantity)
                for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(pk=cart_id).delete()
            order_crated.send_robust(self.__class__, order=order)
            return order


class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "quantity"]

    def validate_product_id(self, cart_id):
        if not Product.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError(f"Product with id '{cart_id}' does not exist")
        return cart_id

    def save(self, **kwargs):
        cart_id = self.context["cart_id"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item

        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id,
                **self.validated_data,
            )

        return self.instance


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["quantity"]
