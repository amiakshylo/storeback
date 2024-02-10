from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'first_name', 'last_name'),
            },
        ),
    )

"""Editing Children Using Generic (универсальние) Relations """
"""We create new custom_store for keepink independancy berween apps"""
class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]
    
admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

    

