from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_password_url = reverse('password_reset:reset-password-request')
    reset_password_url += "?token={}".format(reset_password_token.key)

    email_subject = 'Restovanje lozinke Ant Colony APP'
    email_message = """
    Poštovani,

    Primili smo zahtjev za resetiranje lozinke za vaš račun na Ant Colony APP. Kako biste resetirali lozinku, uđite na stranicu http://127.0.0.1:8000/api/password_reset/confirm/, te kopirajte TOKEN iz sljedećeg URL-a i zalijepite ga u polje za TOKEN (u polje Password unesite novu lozinku):

    {}

    Ako niste zatražili resetiranje lozinke, možete zanemariti ovu poruku.

    Hvala vam.

    Srdačan pozdrav,
    Ant Colony APP tim
    """.format(reset_password_url)

    send_mail(
        subject=email_subject,
        message=email_message,
        from_email='edin.kohnic.20@size.ba',
        recipient_list=[reset_password_token.user.email]
    )
