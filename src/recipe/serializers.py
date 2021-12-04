from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SharecipeUser, Recipe, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharecipeUser
        fields = ["id", "username", "email", "address"]


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["id", "title", "content", "author"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "title", "content", "author", "recipe"]
