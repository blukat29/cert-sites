from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User)
    url = models.CharField(max_length=300)
    text = models.CharField(max_length=10000)
    date = models.DateField()
    # TODO tags
    # TODO images
