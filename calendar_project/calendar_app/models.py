from django.db import models
import datetime

# Create your models here.
class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
