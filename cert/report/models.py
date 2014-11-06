from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Report(models.Model):
    user = models.ForeignKey(User)
    url = models.CharField(max_length=300)
    text = models.CharField(max_length=10000)
    date = models.DateField()
    tags = TaggableManager(blank=True) # Make it not required field.
    # TODO images
