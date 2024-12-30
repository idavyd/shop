from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(Group)
admin.site.register(Profile)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}))