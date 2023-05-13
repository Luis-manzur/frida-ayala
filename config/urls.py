from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from frida_ayala.tickets.views.orders import QReadeTemplateView
from frida_ayala.utils.admin import admin_site

# simple-jwt

urlpatterns = [
                  path('admin/', admin_site.urls),
                  path('qr-reader/', QReadeTemplateView.as_view(), name='qr-reader'),
                  re_path(r'^chaining/', include('smart_selects.urls')),
                  path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
                  path(
                      "docs/",
                      SpectacularSwaggerView.as_view(url_name="api-schema"),
                      name="api-docs",
                  ),
                  path('', include(('frida_ayala.users.urls', 'users'), namespace='users')),
                  path('', include(('frida_ayala.locations.urls', 'locations'), namespace='locations')),
                  path('events/', include(('frida_ayala.events.urls', 'events'), namespace='events')),
                  path('tickets/', include(('frida_ayala.tickets.urls', 'tickets'), namespace='tickets')),
                  path('', include(('frida_ayala.products.urls', 'products'), namespace='products')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)
