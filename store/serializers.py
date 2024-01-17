from tkinter import ALL
from rest_framework import serializers
from decimal import Decimal
from store.models import Customer, Order, Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']
        
    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'inventory',
                'price', 'price_with_tax', 'collection']
    price = serializers.DecimalField(
        # if we rename field we have to linked it with
        max_digits=6, decimal_places=2, source='unit_price')
    # sourse field adding source module in a field paramert
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')  # """for adding aditional field"""
    """Serializing Relationships"""
    """Method 1 (Primary Key)"""
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all())
    """Method 2 (String)"""
    """This methos requies sellecting releted in views module"""
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


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'orders_count']
    orders_count = serializers.IntegerField(read_only=True)
    
    
