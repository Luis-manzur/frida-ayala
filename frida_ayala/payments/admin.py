"""Orders admin panel"""

# Django
from django.contrib import admin

# models
from frida_ayala.payments.models import Payment
# Utils
from frida_ayala.utils.admin import admin_site


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'created', 'status')
    list_filter = ('created',)
    search_fields = ('reference', 'user')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('dni', 'transaction_code', 'amount', 'order_id', 'request_data', 'browser', 'browser_version',
                    'operating_system', 'os_version', 'client_ip', 'response_data', 'reference', 'origin_url', 'status')


admin_site.register(Payment, PaymentAdmin)
