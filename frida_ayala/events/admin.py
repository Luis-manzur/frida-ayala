"""Events admin panel"""
# Django
from django.contrib import admin

# models
from frida_ayala.events.models import Event
from frida_ayala.events.models.movies import Movie
from frida_ayala.events.models.shows import EventDay
from frida_ayala.utils.admin import admin_site


class EventDayInline(admin.TabularInline):
    model = EventDay
    fk = 'event'


class MovieInline(admin.TabularInline):
    model = Movie
    fk = 'show'


class EventAdmin(admin.ModelAdmin):
    inlines = [EventDayInline]
    list_display = ('pk', 'name', 'slug_name')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'start_date', 'end_date', 'venue')


class EventDayAdmin(admin.ModelAdmin):
    inlines = [MovieInline]
    list_display = ('pk', 'date', 'event')
    list_filter = ('start_time', 'end_time', 'date')
    search_fields = ('start_time', 'end_time', 'event')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'duration')
    search_fields = ('name',)


admin_site.register(Movie, MovieAdmin)
admin_site.register(Event, EventAdmin)
admin_site.register(EventDay, EventDayAdmin)