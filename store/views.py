from typing import Collection
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Max, Min, Avg, Sum, Count
from django.db.models.functions import Concat
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from requests import delete, get
from .models import Customer, Product, Collection
from .serializers import CollectionSerializer, CustomerSerializer, ProductSerializer
"""insted of using built-in django classes HttpResponse and HttpResponse
we should use resr_framefork classes
"""
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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


class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem.count() > 0:  # type: ignore
            return Response({'error': 'Product can not be deleted because it is associated with an order item '}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(APIView):
    def get(self, request):
        queryset = Collection.objects.annotate(  # type: ignore
            products_count=Count('products')).all()  # type: ignore
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CollectionDetail(APIView):
    def get(self, request, id):
        collection = get_object_or_404(Collection.objects.annotate(  # type: ignore
            products_count=Count('products')), pk=id)
        serializer = CollectionSerializer(
            collection, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        collection = get_object_or_404(Collection.objects.annotate(  # type: ignore
            products_count=Count('products')), pk=id)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerList(APIView):
    def get(self, request):
        queryset = Customer.objects.annotate(orders_count=Count('orders')).all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetail(APIView):
    def get(self, request, id):
        customer = get_object_or_404(Customer.objects.annotate(
        orders_count=Count('orders')), pk=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id):
        customer = get_object_or_404(Customer.objects.annotate(
        orders_count=Count('orders')), pk=id)
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id):
        customer = get_object_or_404(Customer.objects.annotate(
        orders_count=Count('orders')), pk=id)
        orders_count = customer.orders.count()  # type: ignore
        if orders_count > 0:  # type: ignore
            return Response({'error': f"Customer can not be deleted because it has {orders_count} orders"})
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

