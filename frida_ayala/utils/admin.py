"""Project custom admin site"""

# Django
from django.contrib import admin
from django.contrib.admin import site
from django.shortcuts import render
from django.urls import path


class FAAdminSite(admin.AdminSite):

    def __init__(self, *args, **kwargs):
        super(FAAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(site._registry)  # PART 2

    def qr_reader(self, request):
        context = {}
        return render(request, 'tickets/qr_reader.html', context)

    def each_context(self, request):
        """
        Adds variables to the context of every admin view.
        """
        context = super().each_context(request)
        context['title'] = self.site_title
        context['site_header'] = self.site_header
        context['has_permission'] = self.has_permission(request)
        return context

    def index(self, request, extra_context=None):
        """
        Displays the main admin index page, which includes the app list.
        """
        return super().index(request, extra_context={
            'app_list': self.get_app_list(request),
        })

    def app_index(self, request, app_label, extra_context=None):
        """
        Displays the index page for the given app, which includes the model list.
        """
        return super().app_index(request, app_label, extra_context={
            'app_label': app_label,
            'title': self._get_app_title(app_label),
            'app_list': self.get_app_list(request),
        })

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('qr-reader/', self.admin_view(self.qr_reader), name='qr-reader'),
        ]
        return custom_urls + urls


admin_site = FAAdminSite(name="faadmin")
