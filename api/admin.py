from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile, Product, Category, User
from django.contrib.auth.admin import UserAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


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


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'author', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'author')

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user.username
        obj.save()


admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
