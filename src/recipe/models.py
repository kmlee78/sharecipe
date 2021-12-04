from django.db import models
from django.contrib.auth.models import AbstractUser

class Recipe(models.Model):
    name = models.CharField(max_length=200)

class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

class Methods(models.Model):
    name = models.CharField(max_length=200)
    time = models.IntegerField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

class Theme(models.Model):
    name = models.CharField(max_length=200)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)



# Create your models here.
