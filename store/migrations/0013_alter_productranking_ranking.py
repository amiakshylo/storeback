# Generated by Django 5.0.4 on 2024-05-22 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_productranking_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productranking',
            name='ranking',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
