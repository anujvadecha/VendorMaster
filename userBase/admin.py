from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from userBase.models import NormalUser


@admin.register(NormalUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username','email','is_staff']
    def get_fieldsets(self, request, obj=None):
        if(request.user.is_superuser):
            return  (
                *UserAdmin.fieldsets,
                (
                 'User details',{
                     "fields":('phone_number','profile_picture',
                               'pan_card','is_activated','requested_registration'),
                 }
                )
            )
        else:
            return
            (
            (
                'User details', {
                    "fields": ('phone_number', 'profile_picture',
                               'pan_card', 'is_activated', 'requested_registration'),
                }
            )
        )
