# Generated by Django 5.0.1 on 2024-01-25 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]
