# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gallery.items.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='item',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=gallery.items.fields.ThumbnailImageField(default=b'DEFAULT VALUE', upload_to=b'items'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.items.fields.ThumbnailImageField(upload_to=b'photos'),
        ),
    ]
