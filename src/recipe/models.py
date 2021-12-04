from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import (
    INGREDIENTS,
    THEMES,
    METHODS,
)


class SharecipeUser(User):
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=20)


class Method(models.Model):
    name = models.CharField(max_length=20)


class Theme(models.Model):
    name = models.CharField(max_length=20)


class Recipe(models.Model):
    title = models.CharField(max_length=20, blank=True, default="")
    content = models.TextField()
    author = models.ForeignKey("SharecipeUser", on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeXIngredient")
    methods = models.ManyToManyField(Method, through="RecipeXMethod")
    themes = models.ManyToManyField(Theme, through="RecipeXTheme")
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey("SharecipeUser", on_delete=models.CASCADE)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class RecipeXIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class RecipeXMethod(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Method, on_delete=models.CASCADE)


class RecipeXTheme(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Theme, on_delete=models.CASCADE)
