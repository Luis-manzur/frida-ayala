"""Project custom admin site"""

# Django
from django.contrib import admin


class FAAdminSite(admin.AdminSite):
    pass


admin_site = FAAdminSite(name="faadmin")
