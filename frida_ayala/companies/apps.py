from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CompaniesConfig(AppConfig):
    name = "frida_ayala.companies"
    verbose_name = _("Companies")

    def ready(self):
        try:
            import frida_ayala.companies.signals  # noqa F401
        except ImportError:
            pass
