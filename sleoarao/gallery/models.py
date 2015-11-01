from django.db import models
from django.contrib.auth.models import User

from .items import fields
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = fields.ThumbnailImageField(upload_to='items', blank=True)
    img_exurl = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': 'self.id'})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=200)
    image = fields.ThumbnailImageField(upload_to='photos', blank=True)
    caption = models.CharField(max_length=250, blank=True)
    
    img_exurl = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})
