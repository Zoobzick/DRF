from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    readonly_fields = ['date_joined']


admin.site.register(CustomUser, CustomUserAdmin)
