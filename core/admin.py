from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


"""Editing Children Using Generic Relations """
"""Create new custom_store for keeping independency between apps"""


class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ["tag"]


class CustomProductAdmin(ProductAdmin):
    inlines = [ProductImageInline]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
