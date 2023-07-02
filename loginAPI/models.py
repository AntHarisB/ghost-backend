from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_password_url = "TOKEN = {}".format(reset_password_token.key)

    email_subject = 'Ant Colony APP Password Recovery'
    email_message = """
    Dear All,

    We have received a request to reset the password for your account on Ant Colony APP. 
    Please copy the TOKEN and transfer it to the TOKEN field (enter the new password in the Password field):

    {}

    If you have not requested a password reset, you can ignore this message.

    Thank you.

    Best regards,
    Ant Colony APP Team
    """.format(reset_password_url)

    send_mail(
        subject=email_subject,
        message=email_message,
        from_email='edin.kohnic.20@size.ba',
        recipient_list=[reset_password_token.user.email]
    )
