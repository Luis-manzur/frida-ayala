"""Locations admin panel"""
# Django
from django.contrib import admin

# models
from frida_ayala.locations.models import Venue
from frida_ayala.utils.admin import admin_site


class VenueAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'capacity')
    search_fields = ('name', 'capacity')
    list_filter = ('state__name',)


admin_site.register(Venue, VenueAdmin)
