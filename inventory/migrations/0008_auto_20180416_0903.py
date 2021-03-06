# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20170512_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecrancustomerorders',
            name='customerorders_ptr',
        ),
        migrations.RemoveField(
            model_name='mecranproducttypelotion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mecranproducttyperemover',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mecranproducttypeserum',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mecranproducttypesoap',
            name='category',
        ),
        migrations.RemoveField(
            model_name='waistproductsize',
            name='category',
        ),
        migrations.RemoveField(
            model_name='waistproducttype',
            name='category',
        ),
        migrations.RemoveField(
            model_name='waisttrainercustomerorders',
            name='customerorders_ptr',
        ),
        migrations.AlterModelOptions(
            name='statecountry',
            options={'ordering': ('name',), 'verbose_name_plural': 'states/countries'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[(b'GINGER ME', b'Ginger Me'), (b'COCOA MY KOKO', b'Cocoa My Koko'), (b'GREEN WITH ENVY', b'Green With Envy'), (b'INIGHE', b'Inighe'), (b'LA VIDA LOCA', b'La Vida Loca'), (b'NUTTY BY NATURE', b'Nutty By Nature'), (b'TRIPLE THREAT', b'Triple THreat')], max_length=20),
        ),
        migrations.DeleteModel(
            name='MecranCustomerOrders',
        ),
        migrations.DeleteModel(
            name='MecranProductTypeLotion',
        ),
        migrations.DeleteModel(
            name='MecranProductTypeRemover',
        ),
        migrations.DeleteModel(
            name='MecranProductTypeSerum',
        ),
        migrations.DeleteModel(
            name='MecranProductTypeSoap',
        ),
        migrations.DeleteModel(
            name='WaistProductSize',
        ),
        migrations.DeleteModel(
            name='WaistProductType',
        ),
        migrations.DeleteModel(
            name='WaistTrainerCustomerOrders',
        ),
    ]
