# Generated by Django 5.0.4 on 2024-05-22 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_productranking_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productranking',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rankings', to='store.product'),
        ),
    ]
