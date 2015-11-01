from django.db import models
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.

class Welcome(models.Model):
    Title = models.CharField(max_length=200)
    WelcomeContent = models.TextField()
    TimeStamp = models.DateTimeField()
    ex_imgurl = models.CharField(max_length=300, blank=True)

    Image = models.ImageField(upload_to='covers')

    def __str__(self):
        return self.Title
