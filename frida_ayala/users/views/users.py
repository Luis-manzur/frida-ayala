"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response

# Models
from frida_ayala.users.models import User
from frida_ayala.users.permissions import IsAccountOwner
from frida_ayala.users.serializers import (
    AccountVerificationSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)
# Serializers
from frida_ayala.users.serializers.profiles import ProfileModelSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.
    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(is_active=True, is_client=True)
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_class(self):
        """Assign serializer base on action."""
        if self.action == 'signup':
            return UserSignUpSerializer
        elif self.action == 'verify':
            return AccountVerificationSerializer
        elif self.action in ['retrieve', 'update', 'partial_update']:
            return UserModelSerializer
        elif self.action == 'profile':
            return ProfileModelSerializer

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Felicitaciones, cuenta verificada con éxito!'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user: User = self.get_object()
        profile = user.profileetc_tag_account
        partial = request.method == 'PATCH'
        serializer = self.get_serializer_class()(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)
