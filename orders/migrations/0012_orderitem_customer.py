# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_orderitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]