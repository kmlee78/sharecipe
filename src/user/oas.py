from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from rest_framework import serializers

from user.serializers import UserSerializer


CREATE_BASE_OBJECT = {
    "description": "Reset to default database model setting.",
    "responses": {
        201: OpenApiResponse(
            description="Return 201 when success.",
        )
    },
}

GET_USERS = {
    "description": "Fetch list of all users.",
    "responses": {
        200: OpenApiResponse(
            response=UserSerializer(many=True),
            examples=[
                OpenApiExample(
                    name="example",
                    value=[
                        {
                            "id": 4,
                            "username": "junhcha",
                            "email": "junhcha@example.com",
                            "address": "dormitory",
                            "date_joined": "2021-12-13T19:51:10.387951",
                        },
                        {
                            "id": 5,
                            "username": "kmlee78",
                            "email": "kmlee78@example.com",
                            "address": "dormitory",
                            "date_joined": "2021-12-13T19:51:10.548837",
                        },
                        {
                            "id": 6,
                            "username": "drg1021",
                            "email": "drg1021@example.com",
                            "address": "house",
                            "date_joined": "2021-12-13T19:51:10.681095",
                        },
                    ],
                )
            ],
        )
    },
}


class PostUserBodySerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField()
    password = serializers.CharField()


POST_USER = {
    "description": "Create new account.",
    "request": PostUserBodySerializer,
    "responses": {201: OpenApiResponse(description="Return 201 if success.")},
}

GET_USER_DETAIL = {
    "description": "Get detail information of the user.",
    "responses": {
        200: OpenApiResponse(
            response=UserSerializer,
            examples=[
                OpenApiExample(
                    name="example",
                    value={
                        "id": 4,
                        "username": "junhcha",
                        "email": "junhcha@example.com",
                        "address": "dormitory",
                        "date_joined": "2021-12-13T19:51:10.387951",
                    },
                ),
            ],
        ),
    },
}
