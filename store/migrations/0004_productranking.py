# Generated by Django 5.0.4 on 2024-05-22 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_favoriteproducts_favoriteproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranking', to='store.product')),
            ],
        ),
    ]
