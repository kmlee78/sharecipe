from django.shortcuts import render
from rest_framework.views import APIView
from user.models import SharecipeUser
from user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class UserListView(APIView):
    def get(self, request, format=None):
        users = SharecipeUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class SignUpView(APIView):
    def post(self, request, format=None):
        print(request.data)
        user = SharecipeUser.objects.create_user(
            username=request.data["username"],
            email=request.data["email"],
            address=request.data["address"],
            password=request.data["password"],
        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)


class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return SharecipeUser.objects.get(pk=pk)
        except SharecipeUser.DoesNotExist:
            raise NotFound

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
