from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework.serializers import ModelSerializer

class User(AbstractUser):
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to="profile_pics", blank=True, null=True)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        