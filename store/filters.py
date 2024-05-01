from django_filters.rest_framework import FilterSet
from store.models import Product, Review


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
            'unit_price': ['gt', 'lt']
        }


class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'id': ['exact'],
            'user': ['exact']
        }
