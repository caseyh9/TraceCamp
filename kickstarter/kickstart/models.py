from django.db import models

# Create your models here.
class kickstarter(models.Model):
    backers_count = models.IntegerField()
    blurb = models.TextField()
    category = models.TextField()
    converted_pledged_amount = models.IntegerField()
