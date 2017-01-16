# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0016_deprecate_rendition_filter_relation'),
        ('home', '0004_remove_photopage_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
