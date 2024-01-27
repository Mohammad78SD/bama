from django.db import models

# Create your models here.
class car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    km = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    