# Generated by Django 5.0.4 on 2024-05-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_productranking_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productranking',
            unique_together=set(),
        ),
    ]