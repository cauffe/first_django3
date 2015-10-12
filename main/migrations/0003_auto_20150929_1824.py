# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150929_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbrev',
            field=models.CharField(default=1, max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='capital',
            field=models.CharField(default=1, max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='lat',
            field=models.FloatField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='lon',
            field=models.FloatField(default=1, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(default=1, max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='pop',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
