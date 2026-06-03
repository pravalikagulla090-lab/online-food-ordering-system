from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'phone'),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'phone')}),
    )

admin.site.register(User, CustomUserAdmin)