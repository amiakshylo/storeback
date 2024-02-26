from dataclasses import fields
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode # type: ignore
from django.urls import reverse
from . import models
from .models import ProductImage


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    min_num = 1
    max_num = 5
    autocomplete_fields = ['product']
    extra = 0
    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer', 'payment_status']
    list_editable = ['payment_status']
    list_filter = ['customer']
    

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    filter_1 = '<10'
    filter_2 = '>99'

    def lookups(self, request, model_admin):
        return [
            (self.filter_1, 'Low'),
            (self.filter_2, 'High')
        ]        

    def queryset(self, request, queryset):
        if self.value() == self.filter_1:
            return queryset.filter(inventory__lt=10)
        if self.value() == self.filter_2:
            return queryset.filter(inventory__gt=99)
        

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['thumbnail']
    
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''       
    

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory_action']
    list_display = ['title', 'unit_price',
                    'collection_title', 'inventory_status']
    list_editable = ['unit_price']
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    search_fields = ['title']
    list_per_page = 10
    inlines = [ProductImageInline]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if 0 > product.inventory < 10:
            return 'Low'
        if product.inventory > 99:
            return 'High'
        if product.inventory == 0:
            return 'Empty'
        return 'OK'

    def collection_title(self, product):
        return product.collection.title

    @admin.action(description='Clear inventory')
    def clear_inventory_action(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated',
            messages.ERROR
        )
        
    class Media:
        css = {
            'all': ['store/styles.css']
        }


class CountProductFilter(admin.SimpleListFilter):
    title = 'products'
    parameter_name = 'products'
    filter_1 = '>1'

    def lookups(self, request, model_admin):
        return [
            (self.filter_1, 'Yes'),

        ]

    def queryset(self, request, queryset):
        if self.value() == self.filter_1:
            return queryset.filter(product_count__gt=0)


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    list_filter = [CountProductFilter]
    autocomplete_fields = ['featured_product']
    search_fields = ['title']

    @admin.display(ordering='product_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?' +
            urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('products')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    autocomplete_fields = ['user']

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('orders')
        )

