from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()





