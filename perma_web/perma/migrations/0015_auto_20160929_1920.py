# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-29 19:20
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('perma', '0014_auto_20160916_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrar',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
