from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from userBase.models import NormalUser


@admin.register(NormalUser)
class CustomUserAdmin(UserAdmin):

    def get_user_queryset(self, request=None, queryset=None):
        if (request.user.is_superuser):
            return queryset
        else:
            return queryset.filter(is_activated=True, is_staff=False)

    def get_queryset(self, request):
        queryset = self.model.objects.all()
        return self.get_user_queryset(request=request, queryset=queryset)

    def get_list_display(self, request):
        if (request.user.is_superuser):
            return ['username', 'is_staff', 'is_activated', 'requested_registration']
        else:
            return ['username', 'is_activated', 'phone_number']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User details', {
                "fields": ('phone_number', 'profile_picture',
                           'pan_card', 'is_activated', 'requested_registration'),
            }
        )
    )
    list_filter = ('is_activated', 'requested_registration', 'is_staff')
    list_per_page = 20

    # list_editable = ('is_activated',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        if (request.user.is_superuser):
            self.fieldsets = (
                *UserAdmin.fieldsets,
                (
                    'User details', {
                        "fields": ('phone_number', 'profile_picture',
                                   'pan_card', 'is_activated', 'requested_registration', 'business_card',
                                   'reference_1_name', 'reference_1_mobile'
                                   , 'reference_2_name', 'reference_2_mobile'),
                    }
                )
            )
            return super().get_fieldsets(request, obj)
        else:
            return (
                (
                    'User details', {
                        "fields": ('first_name', 'last_name', 'email', 'phone_number', 'profile_picture',
                                   'pan_card', 'business_card', 'is_activated', 'reference_1_name', 'reference_1_mobile'
                                   , 'reference_2_name', 'reference_2_mobile', 'business_card', 'gst_in_no'),
                    }
                ),
            )
