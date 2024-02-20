

import os
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions

from core import serializers
from .pagination import DefaultPagination
from .filters import ProductFilter, ReviewFilter
from .permissions import CancelOrderPermission, FullDjangoModelPermissions, IsAdminOrReadOnly
from .models import Address, Cart, CartItem, Customer, Order, OrderItem, Product, Collection, Review, ProductImage
from .serializers import AddressSerializer, CartItemSerializer, CartSerializer, CollectionSerializer, CreateOrderSerializer,  CustomerSerializer, \
    OrderSerializer, ProductImageSerializer, ProductSerializer, ReviewSerializer, AddCartItemSerializer, UpdateCartItemSerializer, UpdateOrderSerializer


class ProductImageViewSet(ModelViewSet):

    serializer_class = ProductImageSerializer
    
    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return ProductImage.objects.filter(product_id=product_pk)
        return ProductImage.objects.all()

    def get_serializer_context(self):
        product_pk = self.kwargs.get('product_pk')
        return {'product_id': product_pk} if product_pk is not None else {}
    
    def destroy(self, request, *args, **kwargs):
        image_id = self.kwargs.get('image')
        image = get_object_or_404(ProductImage, image_id)
        try:
            os.remove(image.image.path)  # Assuming 'image' is the field storing the image path
        except FileNotFoundError:
            pass  # If file doesn't exist, just continue
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CartViewSet(CreateModelMixin,
                RetrieveModelMixin,
                DestroyModelMixin,
                GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.prefetch_related('items__product').all()
    permission_classes = [IsAuthenticated]


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
        return {'cart_id': self.kwargs['cart_pk']}


class ProductVievSet(ModelViewSet):  # or ReadOnlyModelViewSet, only for GETing
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        collection_pk = self.kwargs.get('collection_pk')
        if collection_pk is not None:
            return Product.objects.filter(collection_id=collection_pk)
        else:
            return Product.objects.prefetch_related('images').all()

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product can not be deleted because it is associated with an order item '},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': f'Can not be deleted because collection has products'})
        return super().destroy(request, *args, **kwargs)


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
        
    def get_queryset(self):
        user = self.request.user
        if user.is_staff: #type: ignore
            return Address.objects.all()
        else:
            customer_id = Customer.objects.only('id').get(user_id=user.id) #type: ignore
            return Address.objects.filter(customer_id=customer_id)
    
    def get_serializer_context(self, *args, **kwargs):
        customer_pk = self.kwargs.get('customer_pk')
        return {'customer_id': customer_pk}
        
        
        


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.prefetch_related('address').all()
    permission_classes = [FullDjangoModelPermissions]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializers = CustomerSerializer(customer)
            return Response(serializers.data)
        elif request.method == 'PUT':
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
        product_pk = self.kwargs.get('product_pk')
        if product_pk is not None:
            return Review.objects.filter(product_id=product_pk)
        else:
            # Handle the case when 'product_pk' is not present in kwargs
            return Review.objects.all()

    
    def get_serializer_context(self, *args, **kwargs):
        username = self.request.user.username  # type: ignore
        product_id = self.kwargs.get('product_pk')
        return {'product_id': product_id, 'username': username}
    
    


class OrderViewSet(ModelViewSet):
    # http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'option']
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(
            data=request.data,
            context={'user_id': self.request.user.id})  # type: ignore
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  # type: ignore
            return Order.objects.all()
        customer_id = Customer.objects.only(
            'id').get(user_id=user.id)  # type: ignore
        return Order.objects.filter(customer_id=customer_id)
