from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
# simple-jwt
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from frida_ayala.utils.admin import admin_site

urlpatterns = [
                  path('admin/', admin_site.urls),
                  re_path(r'^chaining/', include('smart_selects.urls')),
                  # path('camera_admin/', camera_admin_site.urls),
                  path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
                  path(
                      "docs/",
                      SpectacularSwaggerView.as_view(url_name="api-schema"),
                      name="api-docs",
                  ),
                  path('', include(('frida_ayala.users.urls', 'users'), namespace='users')),
                  path('', include(('frida_ayala.locations.urls', 'locations'), namespace='locations')),
                  path('', include(('frida_ayala.events.urls', 'events'), namespace='events')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
                  # path('', include(('frida_ayala.tickets.urls', 'tickets'), namespace='tickets')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
