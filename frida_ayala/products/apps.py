from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsConfig(AppConfig):
    name = "frida_ayala.products"
    verbose_name = _("Products")

    def ready(self):
        try:
            import frida_ayala.products.signals  # noqa F401
        except ImportError:
            pass
