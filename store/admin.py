from typing import Any
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.db.models.aggregates import Count
from django.http.request import HttpRequest
from . import models


"""Editing Children Using Inlines"""


class OrderItemInline(admin.TabularInline):  # or admin.StackedInline
    model = models.OrderItem
    min_num = 1
    max_num = 5
    autocomplete_fields = ['product']
    """how many rows do we need preloaded"""
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    """Editing Children Using Inlines"""
    inlines = [OrderItemInline]
    """what we gonna see in thiss class"""
    list_display = ['id', 'placed_at', 'customer', 'payment_status']
    """what we gonna edit"""
    list_editable = ['payment_status']
    list_filter = ['customer']


"""Custom filter"""


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    filter_1 = '<10'
    filter_2 = '>99'
    """should takes 2 method"""

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            (self.filter_1, 'Low'),
            (self.filter_2, 'High')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == self.filter_1:
            return queryset.filter(inventory__lt=10)
        if self.value() == self.filter_2:
            return queryset.filter(inventory__gt=99)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """work with form"""
    """show fields"""
    # fields = ['title', 'slug']
    # readonly_fields = ['title']
    # exclude = ['promotions']
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory_action']
    list_display = ['title', 'unit_price',
                    'collection_title', 'inventory_status']
    list_editable = ['unit_price']
    """adding related field"""
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    search_fields = ['title']
    list_per_page = 10

    """computed (исчесляемое поле) field"""
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if 0 > product.inventory < 10:
            return 'Low'
        if product.inventory > 99:
            return 'High'
        if product.inventory == 0:
            return 'Empty'
        return 'OK'
    """adding related field"""

    """computed (исчесляемое поле) field"""

    def collection_title(self, product):
        return product.collection.title

    """Creatin Custom Action"""
    @admin.action(description='Clear inventory')
    def clear_inventory_action(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.ERROR  # from django.contrib import admin, messages
        )


class CountProductFilter(admin.SimpleListFilter):
    title = 'products'
    parameter_name = 'products'
    filter_1 = '>1'
    """should takes 2 method"""

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            (self.filter_1, 'Yes'),

        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == self.filter_1:
            return queryset.filter(product_count__gt=0)


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_filter = [CountProductFilter]
    search_fields = ['title']
    """computed field"""
    """adding sorting"""
    @admin.display(ordering='product_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?' +
            urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            product_count=Count('products')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', "orders"]
    list_editable = ['membership']
    search_fields = ['first_name', 'last_name']
    list_per_page = 10

    """adding link on another page"""
    @admin.display(ordering='orders')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{}</a>', url, customer.orders)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            orders=Count('order')
        )


"""or"""
# admin.site.register(models.Collection, CollectionAdmin())
