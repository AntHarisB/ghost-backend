from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def confirm_password_reset(request):
    token = request.GET.get('token')
    new_password = request.data.get('new_password')

    try:
        reset_token = ResetPasswordToken.objects.get(key=token)
    except ResetPasswordToken.DoesNotExist:
        return Response({'message': 'Invalid token'}, status=400)

    user = get_object_or_404(User, email=reset_token.user.email)

    user.set_password(new_password)
    user.save()

    return Response({'success': 'Password successfully changed'}, status=200)