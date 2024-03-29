"""Users serializers."""

# Utilities
import jwt
# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator
from django.shortcuts import get_object_or_404
# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from frida_ayala.locations.models import Municipality
from frida_ayala.locations.models.states import State
# Models
from frida_ayala.users.models import User, Profile
# Serializers
from frida_ayala.users.serializers.profiles import ProfileModelSerializer
# Tasks
from frida_ayala.users.tasks import send_confirmation_email
# Utilities
from frida_ayala.utils.validators import validate_birth_date


# Simple-jwt


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile'
        )


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.
    Handle sign up data validation and user/profile creation.
    """

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    # Profile
    birth_date = serializers.DateField(required=True, validators=[validate_birth_date], input_formats=['%Y-%m-%d'])
    address = serializers.CharField(max_length=60, required=True)
    municipality = serializers.IntegerField(required=False)
    state = serializers.IntegerField(required=False)
    gender = serializers.ChoiceField(choices=['F', 'M', 'O'])

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)

        if not data.get('municipality'):
            data['municipality'] = None
            data['state'] = None
        return data

    def validate_municipality(self, data):
        municipality = get_object_or_404(Municipality, pk=data)
        return municipality

    def validate_state(self, data):
        state = get_object_or_404(State, pk=data)
        return state

    def get_separated_data(self, data: dict):
        profile_data = dict(list(data.items())[7:])
        user_data = dict(list(data.items())[:7])
        return user_data, profile_data

    def create(self, data):
        """Handle user and profile creation."""
        user_data, profile_data = self.get_separated_data(data)
        user_data.pop('password_confirmation')
        user = User.objects.create_user(**user_data, is_verified=False, is_client=True)
        Profile.objects.create(user=user, **profile_data)
        send_confirmation_email.delay(user_pk=user.pk)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_verified:
            raise serializers.ValidationError("Account is not active yet :(")
        self.context["user"] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
