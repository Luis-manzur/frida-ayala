from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LocationsConfig(AppConfig):
    name = "frida_ayala.tickets"
    verbose_name = _("Tickets")

    def ready(self):
        try:
            import frida_ayala.tickets.signals  # noqa F401
        except ImportError:
            pass
