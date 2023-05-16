"""Orders admin panel"""

# Django
from django.contrib import admin

# Forms
from frida_ayala.products.forms import OrderItemInlineForm, OrderForm
# models
from frida_ayala.products.models import Product, OrderItem, ProductOrder, Category, Size
# Utils
from frida_ayala.utils.admin import admin_site


class SizesInline(admin.TabularInline):
    model = Size
    fk = 'product'


class ProductAdmin(admin.ModelAdmin):
    inlines = [SizesInline]
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
            return ('quantity', 'size', 'product')
        else:
            return ()


class OrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created')
    list_filter = ('created',)
    search_fields = ('code', 'user')

    def get_inlines(self, request, obj):
        if obj:
            return [ProductOrderInline]
        return []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('user', 'code', 'shipping_method', 'payment_method', 'shipping', 'delivery')
        else:
            return ('status',)

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            return OrderForm
        else:
            return super().get_form(request, obj, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin_site.register(Category, CategoryAdmin)
admin_site.register(ProductOrder, OrderAdmin)
admin_site.register(Product, ProductAdmin)
