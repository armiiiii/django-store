from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from django.http.response import JsonResponse

from .models import User, UserSerializer, Feedback, FeedbackSerializer


class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def retrieve_feedbacks(request, prod_id):
    """Returns list queryset of Feedback model for the approptiate product."""

    serializer = FeedbackSerializer(Feedback.objects.filter(product__id__exact = prod_id), many=True)
    return JsonResponse(data=serializer.data, safe=False)
