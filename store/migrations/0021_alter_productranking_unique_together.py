# Generated by Django 5.0.4 on 2024-05-22 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_productranking_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productranking',
            unique_together={('product', 'user')},
        ),
    ]
