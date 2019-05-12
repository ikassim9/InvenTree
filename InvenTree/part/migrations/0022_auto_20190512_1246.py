# Generated by Django 2.2 on 2019-05-12 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('part', '0021_auto_20190510_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='bom_checked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boms_checked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='part',
            name='bom_checked_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='bom_checksum',
            field=models.CharField(blank=True, help_text='Stored BOM checksum', max_length=128),
        ),
    ]
