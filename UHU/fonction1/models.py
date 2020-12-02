#from django.db import models
from djongo import models
# Create your models here.
class Tree(models.Model):
    _id = models.CharField(max_length = 2)
    name = models.CharField(max_length = 100)
    soil_type = models.CharField(max_length = 100)
    family = models.CharField(max_length = 100)
    height = models.CharField(max_length = 100)
    water = models.CharField(max_length = 100)
    size = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)