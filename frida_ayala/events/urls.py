"""Events URLs."""

# Django
from django.urls import include, path
# Django REST Framework
from rest_framework_nested import routers

from frida_ayala.tickets.views import tickets as tickets_views
# Views
from .views import events as events_views
from .views import movies as movies_views
from .views import shows as shows_views
from .views import sponsors as sponsors_views

router = routers.SimpleRouter()
router.register(r'', events_views.EventViewSet, basename='events')

events_router = routers.NestedSimpleRouter(router, r'', lookup='event')
events_router.register(r'shows', shows_views.EventDayViewSet, basename='shows')
events_router.register(r'sponsors', sponsors_views.SponsorViewSet, basename='sponsors')
events_router.register(r'tickets', tickets_views.TicketsViewSet, basename='tickets')

shows_router = routers.NestedSimpleRouter(events_router, r'shows', lookup='show')
shows_router.register(r'movies', movies_views.MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(events_router.urls)),
    path('', include(shows_router.urls)),
]
