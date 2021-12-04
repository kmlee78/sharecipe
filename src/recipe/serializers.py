from rest_framework import serializers
from recipe.models import Ingredient, Method, Recipe, Review, Theme
from user.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ["id", "name"]


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    ingredients = IngredientSerializer(many=True)
    methods = MethodSerializer(many=True)
    themes = ThemeSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "content",
            "author",
            "ingredients",
            "methods",
            "themes",
            "dt_created",
            "dt_updated",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    recipe = RecipeSerializer()

    class Meta:
        model = Review
        fields = [
            "id",
            "title",
            "content",
            "author",
            "recipe",
            "dt_created",
            "dt_updated",
        ]
