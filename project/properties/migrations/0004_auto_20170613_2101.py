# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 21:01
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_properties_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='properties',
            managers=[
                ('search', django.db.models.manager.Manager()),
            ],
        ),
    ]
