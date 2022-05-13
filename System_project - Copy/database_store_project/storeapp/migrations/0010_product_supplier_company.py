# Generated by Django 4.0 on 2022-02-04 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0009_remove_product_supplier_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Supplier_company',
            field=models.ForeignKey(default=1, max_length=200, on_delete=django.db.models.deletion.CASCADE, to='storeapp.supplier'),
            preserve_default=False,
        ),
    ]