import os

from django.contrib.auth.models import AnonymousUser
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Coalesce
from django.db.models import Count, OuterRef, Subquery, IntegerField
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status

from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from likes.models import LikedItem
from store.pagination import DefaultPagination
from store.filters import ProductFilter, ReviewFilter
from store.permissions import FullDjangoModelPermissions, IsAdminOrReadOnly
from store.models import (
    Address,
    Cart,
    CartItem,
    Customer,
    Order,
    OrderItem,
    Product,
    Collection,
    Review,
    ProductImage,
)
from store.serializers import (
    AddressSerializer,
    CartItemSerializer,
    CartSerializer,
    CollectionSerializer,
    CreateOrderSerializer,
    CustomerSerializer,
    OrderSerializer,
    ProductImageSerializer,
    ProductSerializer,
    ReviewSerializer,
    AddCartItemSerializer,
    UpdateCartItemSerializer,
    UpdateOrderSerializer,
)


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        product_pk = self.kwargs.get("product_pk")
        if product_pk:
            return ProductImage.objects.filter(product_id=product_pk)
        return ProductImage.objects.all()

    def create(self, request, *args, **kwargs):
        if "products" not in request.path:
            return Response(
                {"detail": "POST method not allowed here."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().create(request, *args, **kwargs)

    def get_serializer_context(self):
        product_pk = self.kwargs.get("product_pk")
        return {"product_id": product_pk} if product_pk else {}

    def destroy(self, request, *args, **kwargs):
        image_id = self.kwargs.get("pk")
        image = get_object_or_404(ProductImage, pk=image_id)
        image.delete()
        try:
            os.remove(image.image.path)
        except FileNotFoundError:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    serializer_class = CartSerializer
    queryset = Cart.objects.prefetch_related("items__product").all()
    permission_classes = [IsAuthenticated]


class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return CartItem.objects.select_related("product").filter(
            cart_id=self.kwargs["cart_pk"]
        )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        if self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ["title", "description"]
    ordering_fields = ["unit_price", "last_update", "likes_count"]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        product_content_type = ContentType.objects.get_for_model(Product)
        likes_subquery = Subquery(
            LikedItem.objects
            .filter(
                content_type=product_content_type,
                object_id=OuterRef('pk')
            )
            .values('object_id')
            .annotate(cnt=Count('id'))
            .values('cnt')[:1],
            output_field=IntegerField(),
        )

        return (Product.objects
                .prefetch_related("images")
                .annotate(reviews_count=Count("reviews"))
                .annotate(likes_count=Coalesce(likes_subquery, 0)))  # Using Coalesce to ensure zeros instead of NULLs

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=self.kwargs["pk"]) > 0:
            return Response(
                {
                    "error": "Product can not be deleted because it is associated with an order item "
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def like(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        product = self.get_object()
        user = request.user

        liked_item, created = LikedItem.objects.get_or_create(
            user=user,
            content_type=ContentType.objects.get_for_model(Product),
            object_id=product.id
        )

        if created:
            return Response({"message": "Product liked successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Product already liked"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def unlike(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        product = self.get_object()
        user = request.user

        liked_item = LikedItem.objects.filter(
            user=user,
            content_type=ContentType.objects.get_for_model(Product),
            object_id=product.id
        )
        if liked_item.exists():
            liked_item.delete()
            return Response({"message": "Product unliked successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Product not liked yet"}, status=status.HTTP_200_OK)


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        product_count = Product.objects.filter(collection_id=kwargs["pk"]).count()
        if product_count > 0:
            return Response(
                {
                    "error": f"Can not be deleted because collection has {product_count} products"
                }
            )
        return super().destroy(request, *args, **kwargs)


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if "customers" not in request.path:
            return Response(
                {"detail": "POST method not allowed here."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Address.objects.all()
        else:
            customer_id = Customer.objects.only("id").get(user_id=user.id)  # type: ignore
            return Address.objects.filter(customer_id=customer_id)

    def get_serializer_context(self, *args, **kwargs):
        customer_pk = self.request.query_params.get('customer_pk')
        return {"customer_id": customer_pk}


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.prefetch_related("address").all()
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == "GET":
            serializers = CustomerSerializer(customer)
            return Response(serializers.data)
        elif request.method == "PUT":
            serializers = CustomerSerializer(customer, data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ReviewFilter

    def get_queryset(self):
        product_pk = self.kwargs.get("product_pk")
        if product_pk:
            return Review.objects.filter(product_id=product_pk)
        else:
            return Review.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        username = self.request.user.username  # type: ignore
        product_id = self.kwargs.get("product_pk")
        return {"product_id": product_id, "username": username}


class OrderViewSet(ModelViewSet):
    # http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'option']
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ["PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data, context={"user_id": self.request.user.id}
        )  # type: ignore
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer
        elif self.request.method == "PATCH":
            return UpdateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        customer_id = Customer.objects.only("id").get(user_id=user.id)
        return Order.objects.filter(customer_id=customer_id)
