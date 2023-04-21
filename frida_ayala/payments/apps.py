from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsConfig(AppConfig):
    name = "frida_ayala.payments"
    verbose_name = _("Payments")

    def ready(self):
        try:
            import frida_ayala.payments.signals  # noqa F401
        except ImportError:
            pass
