"""Products """

# Django
from django import forms

# Models
from frida_ayala.products.models import OrderItem


class OrderItemInlineForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
