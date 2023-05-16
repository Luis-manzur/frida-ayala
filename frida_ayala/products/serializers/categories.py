"""Categories serializer"""

# Drf
from rest_framework import serializers

# Models
from frida_ayala.products.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Categories model serializer"""
    value = serializers.IntegerField(source='id')
    label = serializers.CharField(source='name')
    checked = serializers.BooleanField(default=False)

    class Meta:
        model = Category
        fields = ['value', 'label', 'checked']
