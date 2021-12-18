import datetime
from re import A

from project_cfg.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from recipe.models import (
    Ingredient,
    Method,
    Recipe,
    RecipeXIngredient,
    RecipeXMethod,
    RecipeXTheme,
    Review,
    Theme,
)
from recipe.serializers import (
    IngredientSerializer,
    MethodSerializer,
    RecipeSerializer,
    ReviewSerializer,
    ThemeSerializer,
)
from recipe import oas
from user.models import SharecipeUser
from django.db import transaction


@extend_schema(tags=["recipe"])
class RecipeList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**oas.GET_RECIPES)
    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    @extend_schema(**oas.POST_RECIPE)
    def post(self, request, format=None):
        user = request.user
        author = SharecipeUser.objects.get(user_ptr_id=user.id)
        ingredients = Ingredient.objects.filter(name__in=request.data["ingredients"])
        methods = Method.objects.filter(name__in=request.data["methods"])
        themes = Theme.objects.filter(name__in=request.data["themes"])
        recipe = Recipe.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            author=author,
        )
        recipe.ingredients.set(ingredients)
        recipe.methods.set(methods)
        recipe.themes.set(themes)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=201)


@extend_schema(tags=["recipe"])
class RecipeDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def _get_object(self, recipe_id):
        try:
            return Recipe.objects.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise NotFound

    @extend_schema(**oas.GET_RECIPE_DETAIL)
    def get(self, request, recipe_id, format=None):
        recipe = self._get_object(recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    @extend_schema(**oas.PUT_RECIPE_CONTENT)
    def put(self, request, recipe_id, format=None):
        recipe = Recipe.objects.get(id=recipe_id)
        ingredients = Ingredient.objects.filter(name__in=request.data["ingredients"])
        methods = Method.objects.filter(name__in=request.data["methods"])
        themes = Theme.objects.filter(name__in=request.data["themes"])

        with transaction.atomic():
            recipe.title = request.data["title"]
            recipe.content = request.data["content"]
            recipe.dt_updated = datetime.datetime.now()
            RecipeXIngredient.objects.filter(recipe=recipe).delete()
            RecipeXIngredient.objects.bulk_create(
                [
                    RecipeXIngredient(recipe=recipe, ingredient=ingredient)
                    for ingredient in ingredients
                ]
            )
            RecipeXMethod.objects.filter(recipe=recipe).delete()
            RecipeXMethod.objects.bulk_create(
                [RecipeXMethod(recipe=recipe, method=method) for method in methods]
            )
            RecipeXTheme.objects.filter(recipe=recipe).delete()
            RecipeXTheme.objects.bulk_create(
                [RecipeXTheme(recipe=recipe, theme=theme) for theme in themes]
            )

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=200)

    @extend_schema(**oas.DELETE_RECIPE)
    def delete(self, request, recipe_id, format=None):
        recipe = self._get_object(recipe_id)
        recipe.delete()
        return Response(status=204)


@extend_schema(tags=["recipe"])
class ReviewAll(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.filter().all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


@extend_schema(tags=["recipe"])
class ReviewList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**oas.GET_REVIEWS)
    def get(self, request, recipe_id, format=None):
        reviews = Review.objects.filter(recipe__id=recipe_id).all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @extend_schema(**oas.POST_REVIEW)
    def post(self, request, recipe_id, format=None):
        user = request.user
        author = SharecipeUser.objects.get(user_ptr_id=user.id)
        recipe = Recipe.objects.get(id=recipe_id)
        title = request.data["title"]
        content = request.data["content"]
        review = Review.objects.create(
            author=author,
            recipe=recipe,
            title=title,
            content=content,
        )

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=201)


@extend_schema(tags=["recipe"])
class ReviewDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def _get_object(self, review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise NotFound

    @extend_schema(**oas.GET_REVIEW_DETAIL)
    def get(self, request, review_id, format=None):
        review = self._get_object(review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    @extend_schema(**oas.PUT_REVIEW_DETAIL)
    def put(self, request, review_id, format=None):
        review = self._get_object(review_id)
        review.title = request.data["title"]
        review.content = request.data["content"]
        review.dt_updated = datetime.datetime.now()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    @extend_schema(**oas.DELETE_REVIEW)
    def delete(self, request, review_id, format=None):
        review = self._get_object(review_id)
        review.delete()
        return Response(status=204)


@extend_schema(tags=["recipe"])
class IngredientList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(**oas.GET_INGREDIENTS)
    def get(self, request, format=None):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    @extend_schema(**oas.POST_INGREDIENTS)
    def post(self, request, format=None):
        ingredient = Ingredient.objects.create(name=request.data["name"])
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data, status=201)


@extend_schema(tags=["recipe"])
class MethodList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(**oas.GET_METHODS)
    def get(self, request, format=None):
        methods = Method.objects.all()
        serializer = MethodSerializer(methods, many=True)
        return Response(serializer.data)

    @extend_schema(**oas.POST_METHODS)
    def post(self, request, format=None):
        method = Method.objects.create(name=request.data["name"])
        serializer = MethodSerializer(method)
        return Response(serializer.data, status=201)


@extend_schema(tags=["recipe"])
class ThemeList(APIView):
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(**oas.GET_THEMES)
    def get(self, request, format=None):
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)

    @extend_schema(**oas.POST_THEMES)
    def post(self, request, format=None):
        theme = Theme.objects.create(name=request.data["name"])
        serializer = ThemeSerializer(theme)
        return Response(serializer.data, status=201)
