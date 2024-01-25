

from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from requests import request
from requests import request
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .pagination import DefaultPagination
from .filters import ProductFilter, ReviewFilter
from .models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection, Review
from .serializers import CartItemSerializer, CartSerializer, CollectionSerializer, CustomerSerializer, OrderItemSerializer, \
OrderSerializer, ProductSerializer, ReviewSerializer, AddCartItemSerializer, UpdateCartItemSerializer


class CartViewSet(CreateModelMixin,
                RetrieveModelMixin,
                DestroyModelMixin,
                GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.prefetch_related('items__product').all()
    
    
class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer    
        if self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs.get('cart_pk')}
    


class ProductVievSet(ModelViewSet):  # or ReadOnlyModelViewSet, only for GETing
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product can not be deleted because it is associated with an order item '},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': f'Can not be deleted because collection has products'})
        return super().destroy(request, *args, **kwargs)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.annotate(
        orders_count=Count('orders')).all()
    serializer_class = CustomerSerializer

    def destroy(self, request, *args, **kwargs):
        if Order.objects.filter(customer_id=kwargs['pk']).count() > 0:
            return Response({'error': f"Customer can not be deleted because it has orders"})
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ReviewFilter

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return Review.objects.filter(product_id=product_pk)
        else:
            # Handle the case when 'product_pk' is not present in kwargs
            return Review.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'product_id': self.kwargs.get('product_pk')}


class OrderViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_pk = self.kwargs.get('customer_pk')
        if customer_pk is not None:
            return Order.objects.filter(customer_id=customer_pk)
        else:
            return Order.objects.select_related('customer').all()
        
class OrderItemVievSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = OrderItemSerializer
    
    def get_queryset(self):
        return OrderItem.objects.select_related('product').filter(order_id=self.kwargs['order_pk'])
