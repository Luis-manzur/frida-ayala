from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LocationsConfig(AppConfig):
    name = "frida_ayala.events"
    verbose_name = _("Events")

    def ready(self):
        try:
            import frida_ayala.events.signals  # noqa F401
        except ImportError:
            pass
