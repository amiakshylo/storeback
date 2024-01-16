from typing import Collection
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Max, Min, Avg, Sum, Count
from django.db.models.functions import Concat
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from requests import delete
from .models import Customer, Product, Collection
from .serializers import CollectionSerializer, CustomerSerializer, ProductSerializer
"""insted of using built-in django classes HttpResponse and HttpResponse
we should use resr_framefork classes
"""
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitem.count() > 0: # type: ignore
            return Response({'error': 'Product can not be deleted because it is associated with an order item '},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, id):
    collection = get_object_or_404(Collection.objects.annotate(
        products_count=Count('products')), pk=id)
    if request.method == 'GET':       
        serializer = CollectionSerializer(collection, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product_count = collection.products.count() # type: ignore
        if product_count > 0:
            return Response({'error': f'Collections can not be deleted because it includes {product_count} products'}) # type: ignore
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def customer_list(request):
    queryset = Customer.objects.annotate(orders_count=Count('orders')).all()
    if request.method == 'GET':
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, id):
    customer = get_object_or_404(Customer.objects.annotate(
        orders_count=Count('orders')), pk=id)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        orders_count = customer.orders.count() # type: ignore
        if orders_count > 0: # type: ignore
            return Response({'error': f"Customer can not be deleted because it has {orders_count} orders"})
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
