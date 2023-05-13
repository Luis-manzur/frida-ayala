"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from frida_ayala.users.models import User, Profile
from frida_ayala.utils.admin import admin_site


class ProfileInline(admin.TabularInline):
    """Inline profile"""
    model = Profile
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    """User model admin."""
    inlines = [
        ProfileInline,
    ]

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_verified')
    list_filter = ('is_active', 'created', 'modified')
    list_editable = ('is_verified',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        fieldsets = super().get_fieldsets(request, obj)
        # Remove the user roles field from the User model fieldsets
        fieldsets[2][1]['fields'] = (
            'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
            'groups',)
        return fieldsets


admin_site.register(User, CustomUserAdmin)
