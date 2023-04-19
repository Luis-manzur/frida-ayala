"""Products """

# Django
from django import forms

# Models
from frida_ayala.products.models import OrderItem, Product


class OrderItemInlineForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(stock__gte=1)
