# Generated by Django 5.0.1 on 2024-01-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]