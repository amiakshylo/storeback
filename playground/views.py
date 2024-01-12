from turtle import update
from typing import Concatenate
from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Max, Min, Avg, Sum, Count
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db import connection
from tags.models import TaggedItem
from store.models import Product
from store.models import Customer
from store.models import OrderItem
from store.models import Collection
from store.models import Order


"""Complex Lookups using q object (AND operator)"""

# @transaction.atomic()


def say_hello(request):
    """Executing RAW sequel queries"""

    # queryset = Product.objects.raw('SELECT * FROM store_product')
    # list(queryset)
    """from django.db import connection"""
    # with connection.cursor() as cursor:
    #     cursor.execute() # type: ignore
    #     """or"""
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    """IF we nedd to make changings together we use from django.db import trasaction. Wich we can use
    ase a decorator on all function or a context manager as below """

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1 # type: ignore
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = -1 # type: ignore
    #     item.quantity = 1
    #     item.unit_price = 10 # type: ignore
    #     item.save()

    """AND operator"""
    # product = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    """or"""
    # product = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    """if we need to use OR operator: from django.db.models import Q(quary) """
    # product = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    """.... OR AND NOT ...."""
    # product = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))
    """Referencing fields using F(field) objects"""
    # product = Product.objects.filter(inventory=F('unit_price'))
    """SORTING DATA"""
    # product = Product.objects.order_by('unit_price', '-title')[0]
    """or"""
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')
    """LIMITATION"""
    # queryset = Product.objects.all()[5:10]
    """RETURN VALUES"""
    # queryset = Product.objects.values('id', 'title').filter(id__lt=10)
    """for JOIN"""
    """return tuples or dictionary with and without sufix _list"""
    # queryset = Product.objects.all().values_list('id', 'title', 'collection__title')
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    """Selected Related objects, 
    select_related: when the object that you're going to be selecting is a single object, so OneToOneField or a ForeignKey
    prefetch_related: when you're going to get a "set" of things, so ManyToManyFields as you stated or reverse ForeignKeys."""
    # products = Product.objects.select_related('collection')
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    """exercise"""
    # queryset = Order.objects.select_related('customer').prefetch_related(
    #     'orderitem_set__product').order_by('-placed_at')[:5]
    """Aggregated object (Agregate function)"""
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    """exercise"""
    # result = Product.objects.filter(collection_id=3).aggregate(min_price=Min('unit_price'),
    #                                                            max_price=Max('unit_price'), avg_price=Avg('unit_price'))
    """Annotating Object"""

    # result = Product.objects.annotate(new_id=F('id') + 1)
    # result = Product.objects.annotate(new_colum=Value('id'))

    """Concatinating object"""
    """long way"""
    # concat = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    """short_way"""
    # concat = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    """ExpressionWrapper for complex expression (annotation) from django.db.models import ExpressionWrapper"""
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # new_price = Product.objects.annotate(
    #     discounted_price=discounted_price
    #     )

    """Querying Generic Relationships"""
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )
    """Instead of using belows we can creat a custom manager class ()"""
    # queryset = TaggedItem.objects.get_tags_for(Product(), 1) # type: ignore
    # return render(request, 'hello.html', {'name': 'Andrew', 'orders': queryset})

    """Creating object"""

    # collection = Collection()
    # collection.title = 'Movie'
    # collection.featured_product = Product(pk=1) # type: ignore
    # collection.save()

    """Updating object"""
    # Collection.objects.filter(pk=11).update(title="Movie")

    """Deleting object"""
    # Collection.objects.filter(pk=11).delete()

    return render(request, 'hello.html', {'name': 'Andrew'})
