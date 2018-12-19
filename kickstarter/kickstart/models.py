from django.db import models

# Create your models here.
class kickstarter(models.Model):
    backers_count = IntegerField()
    blurb = TextField()
    category = TextField()
    # Rest of the fields???
