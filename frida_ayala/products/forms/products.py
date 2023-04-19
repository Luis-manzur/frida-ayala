"""Products """

# Django
from django import forms

# Models
from frida_ayala.products.models import OrderItem


class OrderItemInlineForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(product__stock__gte=1)
        return qs
