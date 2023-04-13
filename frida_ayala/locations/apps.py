from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LocationsConfig(AppConfig):
    name = "frida_ayala.locations"
    verbose_name = _("Locations")

    def ready(self):
        try:
            import frida_ayala.locations.signals  # noqa F401
        except ImportError:
            pass
