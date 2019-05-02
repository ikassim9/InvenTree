# Generated by Django 2.2 on 2019-05-01 13:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0007_auto_20190429_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, 'Pending'), (30, 'Cancelled'), (40, 'Complete')], default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='builditem',
            name='build',
            field=models.ForeignKey(help_text='Build to allocate parts', on_delete=django.db.models.deletion.CASCADE, related_name='allocated_stock', to='build.Build'),
        ),
    ]