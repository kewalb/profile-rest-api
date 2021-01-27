from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)