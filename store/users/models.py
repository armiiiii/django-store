from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to="profile_pics", blank=True, null=True)


class Feedback(models.Model):
    class Rating(models.IntegerChoices):
        one_star = 1
        two_stars = 2
        three_stars = 3
        four_stars = 4
        five_stars = 5
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("goods.Product", on_delete=models.CASCADE)
    pros = models.TextField(null=False, blank=False, validators=[MinLengthValidator(10)])
    cons = models.TextField(null=False, blank=False, validators=[MinLengthValidator(10)])
    comment = models.TextField(null=False, blank=False, validators=[MinLengthValidator(10)])
    rating = models.IntegerField(choices=Rating, null=False, blank=False)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ["product"]
