# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gallery.items.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20151028_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=gallery.items.fields.ThumbnailImageField(upload_to=b'items', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.items.fields.ThumbnailImageField(upload_to=b'photos', blank=True),
        ),
    ]
