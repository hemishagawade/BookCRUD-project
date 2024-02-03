from django.db import models

# Create your models here.
# model - database table structure
class Book(models.Model):
    # id - auto genenrated
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
