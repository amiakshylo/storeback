# Generated by Django 5.0.4 on 2024-05-07 14:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_cartitem_quantity_favoriteproducts'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteProducts',
            new_name='FavoriteProduct',
        ),
    ]