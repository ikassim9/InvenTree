# Generated by Django 3.0.5 on 2020-06-04 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_remove_supplierpart_manufacturer_name'),
        ('stock', '0044_auto_20200528_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='customer',
            field=models.ForeignKey(help_text='Customer', limit_choices_to={'is_customer': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_stock', to='company.Company', verbose_name='Customer'),
        ),
    ]
