from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from userBase.models import NormalUser


@admin.register(NormalUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username','email','is_staff']