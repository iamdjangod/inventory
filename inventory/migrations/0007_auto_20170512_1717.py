# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20170511_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockvalues',
            name='hairnownow_value',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='stockvalues',
            name='hairnymph_value',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='stockvalues',
            name='molatoo_lotion_value',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='stockvalues',
            name='molatoo_serum_value',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
