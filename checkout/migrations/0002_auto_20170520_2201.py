# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 01:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('cart_key', 'product')]),
        ),
    ]
