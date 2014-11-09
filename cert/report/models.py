from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Report(models.Model):
    user = models.ForeignKey(User)
    url = models.CharField(max_length=300)
    text = models.CharField(max_length=10000)
    date = models.DateField()
    tags = TaggableManager(blank=True) # Make it not required field.
    image1 = models.FileField(upload_to='images/%Y/%m', blank=True, default="")
    image2 = models.FileField(upload_to='images/%Y/%m', blank=True, default="")
    image3 = models.FileField(upload_to='images/%Y/%m', blank=True, default="")
    image4 = models.FileField(upload_to='images/%Y/%m', blank=True, default="")
