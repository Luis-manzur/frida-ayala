"""Events URLs."""

# Django
from django.urls import include, path
# Django REST Framework
from rest_framework_nested import routers

# Views
from .views import events as events_views
from .views import movies as movies_views
from .views import shows as shows_views

router = routers.SimpleRouter()
router.register(r'events', events_views.EventViewSet, basename='events')

events_router = routers.NestedSimpleRouter(router, r'events', lookup='event')
events_router.register(r'shows', shows_views.EventDayViewSet, basename='shows')

shows_router = routers.NestedSimpleRouter(events_router, r'shows', lookup='show')
shows_router.register(r'movies', movies_views.MovieViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(events_router.urls)),
    path('', include(shows_router.urls)),

]
