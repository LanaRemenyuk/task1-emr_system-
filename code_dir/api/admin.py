from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import PatientAdminForm
from .models import CustomUser, Patient


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Role", {"fields": ("role",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "role",
                ),
            },
        ),
    )
    search_fields = ("username", "email", "role")
    ordering = ("username",)


class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm
    list_display = ("id", "date_of_birth", "diagnoses", "created_at")
    list_filter = ("created_at",)
    search_fields = ("id", "diagnoses")
    ordering = ("-created_at",)
    exclude = ("diagnoses",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient, PatientAdmin)
