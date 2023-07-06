from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site


@permission_classes([AllowAny])
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    reset_password_url = f'http://localhost:3000/forgotPassword?token={reset_password_token.key}'

    email_subject = 'Ant Colony APP Password Recovery'
    email_message = f"""
    Dear All,

    We have received a request to reset the password for your account on Ant Colony APP. 
    Please click the following link to reset your password:

    {reset_password_url}

    If you have not requested a password reset, you can ignore this message.

    Thank you.

    Best regards,
    Ant Colony APP Team
    """

    send_mail(
        subject=email_subject,
        message=email_message,
        from_email='edin.kohnic.20@size.ba',
        recipient_list=[reset_password_token.user.email]
    )

