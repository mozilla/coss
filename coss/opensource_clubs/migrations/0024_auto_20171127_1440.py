# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensource_clubs', '0023_aboutpage_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entitydetailpage',
            old_name='description_link',
            new_name='body_link',
        ),
        migrations.RenameField(
            model_name='entitydetailpage',
            old_name='description',
            new_name='body_text',
        ),
    ]
