# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20151021_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img_exurl',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=300),
        ),
        migrations.AddField(
            model_name='photo',
            name='img_exurl',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=300),
        ),
    ]
