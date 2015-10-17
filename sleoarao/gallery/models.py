from django.db import models
from .items import fields
# Create your models here.


class Users(models.Model):
    """
    Classfy the Gallery by Username.
    """
    username = models.CharField(max_length=200)

    class meta:
        ordering = ['username']

    def __str__(self):
        return self.name


class Item(models.Model):
    username = models.ForeignKey(Users)
    name= models.CharField(max_length=250)
    description = models.TextField()
    timestamp = models.DateField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': 'self.id'})

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=200)
    image = fields.ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})
