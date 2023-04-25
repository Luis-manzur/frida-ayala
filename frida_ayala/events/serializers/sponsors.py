"""Sponsors Serializers"""

# Django REST Framework
from rest_framework import serializers

# Serializers
from frida_ayala.companies.serializers import CompanyModelSerializer
# Models
from frida_ayala.events.models import Sponsor


class SponsorModelSerializer(serializers.ModelSerializer):
    """Sponsor model serializer."""
    company = CompanyModelSerializer(read_only=True)

    class Meta:
        model = Sponsor
        exclude = ['created', 'modified', 'arrangement', 'event']
