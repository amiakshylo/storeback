
from django.forms import CharField, ValidationError
from store.signals import order_crated
from rest_framework import serializers
from decimal import Decimal
from django.db import transaction
from .models import Address, Cart, CartItem, Customer, Order, OrderItem, Product, Collection, ProductImage, Review


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']
        
    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)
        
        


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'date', 'description']
        
    user = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        product_id = self.context['product_id']
        user = self.context['username']
        return Review.objects.create(product_id=product_id, user=user, **validated_data)
        


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory',
                'price', 'price_with_tax', 'collection', 'reviews_count']
    price = serializers.DecimalField(
        # if we rename field we have to linked it with
        max_digits=6, decimal_places=2, source='unit_price')
    # sourse field adding source module in a field paramert
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')  # """for adding aditional field"""
    reviews_count = serializers.IntegerField(read_only=True)
    """Serializing Relationships"""
    """Method 1 (Primary Key)"""
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all())
    """Method 2 (String)"""
    """This methods requies sellecting releted in views module"""
    # collection = serializers.StringRelatedField()
    """Method 3"""
    """nested object"""
    # collection = CollectionSerializer()
    """Method 4 (hyperlink)"""
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )

    """for adding aditional field"""

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

    """Validation data example"""
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwort do not match')
    #     return data


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.unit_price


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

    def get_total_price(self, cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])


class AddressSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    class Meta:
        model = Address       
        fields = ['id', 'street', 'city', 'customer_id']

class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    address = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user_id',
                'phone', 'birth_date', 'membership', 'address']
        
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['payment_status']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'payment_status', 'placed_at']
        

class CreateOrderSerializer(serializers.Serializer):
    
    cart_id = serializers.UUIDField()
    
    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('Cart id does not exist')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty')
        return cart_id
    
        
    
    def save(self, **kwargs):
        with transaction.atomic():
            cart_id = self.validated_data['cart_id'] # type: ignore
            customer = Customer.objects.get(
                user_id=self.context['user_id'])           
            order = Order.objects.create(customer=customer)
            cart_items = CartItem.objects.select_related('product').filter(cart_id=cart_id)
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                ) for item in cart_items
                ]
            OrderItem.objects.bulk_create(order_items)
            Cart.objects.filter(pk=cart_id).delete()
            
            order_crated.send_robust(self.__class__, order=order)
            
            return order
            
        





class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']  # type: ignore
        quantity = self.validated_data['quantity']  # type: ignore

        try:
            cart_item = CartItem.objects.get(
                cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item

        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data)  # type: ignore

        return self.instance

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
