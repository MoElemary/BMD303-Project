# Generated by Django 4.0 on 2022-05-13 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0015_patient_remove_order_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Patient_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storeapp.patient'),
            preserve_default=False,
        ),
    ]
