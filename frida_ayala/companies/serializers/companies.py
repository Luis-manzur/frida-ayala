"""Company serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from frida_ayala.companies.models import Company


class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['created', 'modified']
