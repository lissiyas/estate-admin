# Generated by Django 5.0 on 2023-12-21 15:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='agreement_end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tenant',
            name='monthly_rent_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tenant',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estate_admin.property'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='unit_type',
            field=models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')], default='1BHK', max_length=5),
        ),
        migrations.DeleteModel(
            name='RentalAgreement',
        ),
    ]