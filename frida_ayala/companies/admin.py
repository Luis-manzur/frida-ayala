"""Companies admin panel"""
# Django
from django.contrib import admin

# models
from frida_ayala.companies.models import Companies, Contact
from frida_ayala.utils.admin import admin_site


class ContactInline(admin.StackedInline):
    model = Contact
    fk_name = 'company'


class CompanyAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ('name', 'rif', 'sector', 'contact')
    list_filter = ('sector',)
    search_fields = ('name', 'rif', 'sector', 'contact')


admin_site.register(Companies, CompanyAdmin)
