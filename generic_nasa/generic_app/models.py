from django.db import models

# Create your models here.
class NasaComment(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    image_url = models.URLField()
    date = models.DateField()
