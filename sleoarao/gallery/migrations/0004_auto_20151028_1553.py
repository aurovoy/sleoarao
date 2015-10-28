# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20151025_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img_exurl',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img_exurl',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
