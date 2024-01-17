from typing import Collection
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Max, Min, Avg, Sum, Count
from django.db.models.functions import Concat
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from requests import delete, get
from .models import Customer, Order, OrderItem, Product, Collection, Review
from .serializers import CollectionSerializer, CustomerSerializer, ProductSerializer, ReviewSerializer
"""insted of using built-in django classes HttpResponse and HttpResponse
we should use resr_framefork classes
"""
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

"""implementation with mixin and ListCreateAPIView"""


class ProductVievSet(ModelViewSet):  # or ReadOnlyModelViewSet, only for GETing
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product can not be deleted because it is associated with an order item '}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    """If we wanna have some logic for creating queryset or serializer
    for example some condition"""
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()

    # def get_serializer_class(self):
    #     return ProductSerializer


"""implementation with APIView class"""
# class ProductList(APIView):
#     def get(self, request):
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

"""Long method"""
# @api_view(['GET', 'POST'])
# def product_list(request):
# if request.method == 'GET':
#     queryset = Product.objects.select_related('collection').all()
#     serializer = ProductSerializer(queryset, many=True, context={'request': request})
#     return Response(serializer.data)
# elif request.method == 'POST':
#     serializer = ProductSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(  # type: ignore
        products_count=Count('products')).all()  # type: ignore
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': f'Can not be deleted because collection has products'})
        
        return super().destroy(request, *args, **kwargs)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.annotate(
        orders_count=Count('orders')).all()
    serializer_class = CustomerSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Order.objects.filter(customer_id=kwargs['pk']).count() > 0:  # type: ignore
            return Response({'error': f"Customer can not be deleted because it has orders"})
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
