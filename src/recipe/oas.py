from django.db.models.fields import CharField
from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from rest_framework import serializers

from recipe.serializers import (
    IngredientSerializer,
    MethodSerializer,
    RecipeSerializer,
    ReviewSerializer,
    ThemeSerializer,
)


GET_RECIPES = {
    "description": "fetch list of all recipes.",
    "responses": {
        200: OpenApiResponse(
            response=RecipeSerializer(many=True),
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {
                            "id": 2,
                            "title": "Cup Ramen",
                            "content": "1. Boil water.\n 2. Pour water into Cup Ramen.\n 3. wait 4 minutes. \n 4. Eat.",
                            "author": {
                                "id": 5,
                                "username": "kmlee78",
                                "email": "kmlee78@example.com",
                                "address": "dormitory",
                                "date_joined": "2021-12-13T19:51:10.548837",
                            },
                            "ingredients": [{"id": 58, "name": "water"}],
                            "methods": [{"id": 9, "name": "boil"}],
                            "themes": [{"id": 9, "name": "party"}],
                            "dt_created": "2021-12-13T19:51:10.816215",
                            "dt_updated": "2021-12-13T19:51:10.816245",
                        }
                    ],
                )
            ],
        )
    },
}


class PostRecipeBodySerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    ingredients = serializers.ListField()
    methods = serializers.ListField()
    themes = serializers.ListField()


POST_RECIPE = {
    "description": "Create new recipe. Signin required.",
    "request": PostRecipeBodySerializer,
    "responses": {
        201: OpenApiResponse(
            description="Return 201 if success",
        ),
    },
}

GET_RECIPE_DETAIL = {
    "description": "Get recipe detail.",
    "responses": {
        200: OpenApiResponse(
            response=RecipeSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value={
                        "id": 2,
                        "title": "Cup Ramen",
                        "content": "1. Boil water.\n 2. Pour water into Cup Ramen.\n 3. wait 4 minutes. \n 4. Eat.",
                        "author": {
                            "id": 5,
                            "username": "kmlee78",
                            "email": "kmlee78@example.com",
                            "address": "dormitory",
                            "date_joined": "2021-12-13T19:51:10.548837",
                        },
                        "ingredients": [{"id": 58, "name": "water"}],
                        "methods": [{"id": 9, "name": "boil"}],
                        "themes": [{"id": 9, "name": "party"}],
                        "dt_created": "2021-12-13T19:51:10.816215",
                        "dt_updated": "2021-12-13T19:51:10.816245",
                    },
                ),
            ],
        )
    },
}


class PutRecipeBody(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    ingredients = serializers.ListField()
    methods = serializers.ListField()
    themes = serializers.ListField()


PUT_RECIPE_CONTENT = {
    "description": "Update recipe contents.",
    "request": PutRecipeBody,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}

DELETE_RECIPE = {
    "description": "Delete recipe.",
    "responses": {204: OpenApiResponse(description="Return 204 if success.")},
}

GET_REVIEWS = {
    "description": "Fetch list of the certain recipe reviews.",
    "responses": {
        200: OpenApiResponse(
            response=ReviewSerializer(many=True),
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {
                            "id": 2,
                            "title": "Good!",
                            "content": "I love Ramen.",
                            "author": {
                                "id": 6,
                                "username": "drg1021",
                                "email": "drg1021@example.com",
                                "address": "house",
                                "date_joined": "2021-12-13T19:51:10.681095",
                            },
                            "recipe": {
                                "id": 2,
                                "title": "Cup Ramen",
                                "content": "1. Boil water.\n 2. Pour water into Cup Ramen.\n 3. wait 4 minutes. \n 4. Eat.",
                                "author": {
                                    "id": 5,
                                    "username": "kmlee78",
                                    "email": "kmlee78@example.com",
                                    "address": "dormitory",
                                    "date_joined": "2021-12-13T19:51:10.548837",
                                },
                                "ingredients": [{"id": 58, "name": "water"}],
                                "methods": [{"id": 9, "name": "boil"}],
                                "themes": [{"id": 9, "name": "party"}],
                                "dt_created": "2021-12-13T19:51:10.816215",
                                "dt_updated": "2021-12-13T19:51:10.816245",
                            },
                            "dt_created": "2021-12-13T19:51:10.850415",
                            "dt_updated": "2021-12-13T19:51:10.850457",
                        }
                    ],
                )
            ],
        )
    },
}


class PostReviewBody(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


POST_REVIEW = {
    "description": "Create new review.",
    "request": PostReviewBody,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}

GET_REVIEW_DETAIL = {
    "description": "Get review detail.",
    "responses": {
        200: OpenApiResponse(
            response=ReviewSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value={
                        "id": 2,
                        "title": "Good!",
                        "content": "I love Ramen.",
                        "author": {
                            "id": 6,
                            "username": "drg1021",
                            "email": "drg1021@example.com",
                            "address": "house",
                            "date_joined": "2021-12-13T19:51:10.681095",
                        },
                        "recipe": {
                            "id": 2,
                            "title": "Cup Ramen",
                            "content": "1. Boil water.\n 2. Pour water into Cup Ramen.\n 3. wait 4 minutes. \n 4. Eat.",
                            "author": {
                                "id": 5,
                                "username": "kmlee78",
                                "email": "kmlee78@example.com",
                                "address": "dormitory",
                                "date_joined": "2021-12-13T19:51:10.548837",
                            },
                            "ingredients": [{"id": 58, "name": "water"}],
                            "methods": [{"id": 9, "name": "boil"}],
                            "themes": [{"id": 9, "name": "party"}],
                            "dt_created": "2021-12-13T19:51:10.816215",
                            "dt_updated": "2021-12-13T19:51:10.816245",
                        },
                        "dt_created": "2021-12-13T19:51:10.850415",
                        "dt_updated": "2021-12-13T19:51:10.850457",
                    },
                )
            ],
        )
    },
}


PUT_REVIEW_DETAIL = {
    "description": "Update review contents.",
    "request": PostReviewBody,
    "responses": {200: OpenApiResponse(description="Reutrn 200 if success.")},
}

DELETE_REVIEW = {
    "description": "Delete review.",
    "responses": {204: OpenApiResponse(description="Return 204 if success.")},
}


class PostEnumBody(serializers.Serializer):
    name = serializers.CharField()


GET_INGREDIENTS = {
    "description": "Fetch list of all available ingredients.",
    "responses": {
        200: OpenApiResponse(
            response=IngredientSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {"id": 31, "name": "carrot"},
                        {"id": 32, "name": "onion"},
                        {"id": 33, "name": "potato"},
                        {"id": 34, "name": "tomato"},
                        {"id": 35, "name": "brocoli"},
                        {"id": 36, "name": "mushroom"},
                        {"id": 37, "name": "garlic"},
                        {"id": 38, "name": "leek"},
                        {"id": 39, "name": "cabbage"},
                        {"id": 40, "name": "bean"},
                        {"id": 41, "name": "kimchi"},
                        {"id": 42, "name": "egg"},
                        {"id": 43, "name": "beef"},
                        {"id": 44, "name": "chicken"},
                        {"id": 45, "name": "pork"},
                        {"id": 46, "name": "fish"},
                        {"id": 47, "name": "sausage"},
                        {"id": 48, "name": "salt"},
                        {"id": 49, "name": "sugar"},
                        {"id": 50, "name": "vinegar"},
                        {"id": 51, "name": "soy sauce"},
                        {"id": 52, "name": "oil"},
                        {"id": 53, "name": "pepper"},
                        {"id": 54, "name": "noodle"},
                        {"id": 55, "name": "rice"},
                        {"id": 56, "name": "bread"},
                        {"id": 57, "name": "flour"},
                        {"id": 58, "name": "water"},
                        {"id": 59, "name": "milk"},
                        {"id": 60, "name": "cheese"},
                    ],
                )
            ],
        )
    },
}

GET_METHODS = {
    "description": "Fetch list of all available methods.",
    "responses": {
        200: OpenApiResponse(
            response=MethodSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {"id": 9, "name": "boil"},
                        {"id": 10, "name": "roast"},
                        {"id": 11, "name": "steam"},
                        {"id": 12, "name": "fry"},
                        {"id": 13, "name": "bake"},
                        {"id": 14, "name": "dry"},
                        {"id": 15, "name": "torch"},
                        {"id": 16, "name": "freeze"},
                    ],
                )
            ],
        )
    },
}

GET_THEMES = {
    "description": "Fetch list of all available themes.",
    "responses": {
        200: OpenApiResponse(
            response=ThemeSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {"id": 9, "name": "party"},
                        {"id": 10, "name": "meal"},
                        {"id": 11, "name": "entertainment"},
                        {"id": 12, "name": "nurse"},
                        {"id": 13, "name": "snack"},
                        {"id": 14, "name": "supper"},
                        {"id": 15, "name": "exercise"},
                        {"id": 16, "name": "diet"},
                    ],
                )
            ],
        )
    },
}

POST_INGREDIENTS = {
    "description": "Create new ingredients option.",
    "request": PostEnumBody,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}
POST_METHODS = {
    "description": "Create new methods option.",
    "request": PostEnumBody,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}
POST_THEMES = {
    "description": "Create new themes option.",
    "request": PostEnumBody,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}
