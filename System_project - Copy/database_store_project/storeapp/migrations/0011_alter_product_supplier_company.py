# Generated by Django 4.0 on 2022-02-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0010_product_supplier_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Supplier_company',
            field=models.CharField(max_length=150),
        ),
    ]
