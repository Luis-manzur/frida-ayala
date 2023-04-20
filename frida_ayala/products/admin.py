"""Orders admin panel"""

# Django
from django.contrib import admin

# Forms
from frida_ayala.products.forms import OrderItemInlineForm, OrderForm
# models
from frida_ayala.products.models import Product, OrderItem, ProductOrder
# Utils
from frida_ayala.utils.admin import admin_site


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'price')
    list_filter = ('supplier__name',)
    search_fields = ('type', 'price', 'event')


class ProductOrderInline(admin.TabularInline):
    model = OrderItem
    fk = 'order'
    form = OrderItemInlineForm

    def get_extra(self, request, obj=None):
        if obj:
            return 0
        else:
            return 3

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(stock__gte=1)
    #     return qs

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('quantity',)
        else:
            return ()


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]
    list_display = ('code', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('code', 'user')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('user', 'code')
        else:
            return ('status',)

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return OrderForm
        else:
            return super().get_form(request, obj, **kwargs)


admin_site.register(ProductOrder, OrderAdmin)
admin_site.register(Product, ProductAdmin)
