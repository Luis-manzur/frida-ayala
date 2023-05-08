"""Brand serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.companies.models import Company


class BrandSerializer(serializers.ModelSerializer):
    """Ticket model serializer"""
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = Company
        fields = ['value', 'label', 'checked']
