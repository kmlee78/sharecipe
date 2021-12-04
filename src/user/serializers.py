from rest_framework import serializers
from user.models import SharecipeUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharecipeUser
        fields = ["id", "username", "email", "address", "date_joined"]
