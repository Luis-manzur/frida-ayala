"""Product orders forms"""

# Django
from django import forms

# Models
from frida_ayala.products.models import ProductOrder


class OrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['user']
