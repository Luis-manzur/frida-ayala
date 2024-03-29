"""Celery tasks."""

from __future__ import absolute_import, unicode_literals

from datetime import timedelta

import jwt
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

from frida_ayala.users.models import User


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        "user": user.username,
        "exp": int(exp_date.timestamp()),
        "type": "email_confirmation",
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


@shared_task()
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = "Bienvenido @{}! Verifica tu cuenta antes de empezar a utilizar fridaayala.com.".format(
        user.username
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    content = render_to_string(
        "emails/users/account_verification.html",
        {"token": verification_token, "user": user},
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()
