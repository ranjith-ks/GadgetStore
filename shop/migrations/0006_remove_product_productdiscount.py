# Generated by Django 4.0.3 on 2022-05-05 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_producturl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productDiscount',
        ),
    ]
