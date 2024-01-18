from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from store.filters import ProductFilter
from rest_framework.filters import SearchFilter
from .models import Customer, Order, OrderItem, Product, Collection, Review
from .serializers import CollectionSerializer, CustomerSerializer, ProductSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ProductVievSet(ModelViewSet):  # or ReadOnlyModelViewSet, only for GETing
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product can not be deleted because it is associated with an order item '}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


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
        # type: ignore
        if Order.objects.filter(customer_id=kwargs['pk']).count() > 0:
            return Response({'error': f"Customer can not be deleted because it has orders"})
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    # queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
