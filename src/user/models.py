from django.contrib.auth.models import User
from django.db import models


class SharecipeUser(User):
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.username
