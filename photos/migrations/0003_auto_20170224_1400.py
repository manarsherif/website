# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170224_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='features',
            field=models.FileField(blank=True, upload_to='./photos/media/features/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='./photos/media/photos/'),
        ),
    ]
