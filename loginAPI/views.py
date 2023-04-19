from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


    # User = get_user_model()

    # user = User.objects.create_user(
    #     username='johndoe',
    #     email='johndoe@.com',
    #     password='abc123456'
    # )

    # user.save()