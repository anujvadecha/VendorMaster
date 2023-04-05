# -*- coding: utf-8 -*-
from VendorMaster import settings
from admin_interface.models import Theme

import django
from django.contrib import admin

from vendorbase.models import Vendor

if django.VERSION < (2, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


class ThemeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ThemeAdmin, self).get_queryset(request)
        if (request.user.is_superuser):
            return qs
        else:
            return qs.filter(vendor = Vendor.objects.filter(user_id=request.user).first())

    def get_readonly_fields(self, request, obj=None):
        if (request.user.is_superuser):
            return ()
        else:
            return ('vendor','name')

    list_display = ('name', 'active',)
    list_editable = ('active',)
    list_per_page = 100
    show_full_result_count = False

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'active',)
        }),
        (_('Vendor'), {
            'classes': ('wide',),
            'fields': (
                'vendor',
            )
        }),
        (_('Logo'), {
            'classes': ('wide',),
            'fields': (
                'logo',
                'logo_color',
                'logo_visible',
                'background_image'
            )
        }),
        (_('Favicon'), {
            'classes': ('wide',),
            'fields': ('favicon',)
        }),
        (_('Title'), {
            'classes': ('wide',),
            'fields': (
                'title',
                'title_color',
                'title_visible',
            )
        }),
        (_('Header'), {
            'classes': ('wide',),
            'fields': (
                'css_header_background_color',
                'css_header_text_color',
                'css_header_link_color',
                'css_header_link_hover_color',
            )
        }),
        (_('Breadcrumbs / Module headers'), {
            'classes': ('wide',),
            'fields': (
                'css_module_background_color',
                'css_module_text_color',
                'css_module_link_color',
                'css_module_link_hover_color',
                'css_module_rounded_corners',
            )
        }),
        (_('Generic Links'), {
            'classes': ('wide',),
            'fields': (
                'css_generic_link_color',
                'css_generic_link_hover_color',
            )
        }),
        (_('Save Buttons'), {
            'classes': ('wide',),
            'fields': (
                'css_save_button_background_color',
                'css_save_button_background_hover_color',
                'css_save_button_text_color',
            )
        }),
        (_('Delete Buttons'), {
            'classes': ('wide',),
            'fields': (
                'css_delete_button_background_color',
                'css_delete_button_background_hover_color',
                'css_delete_button_text_color',
            )
        }),
        (_('List Filter'), {
            'classes': ('wide',),
            'fields': (
                'list_filter_dropdown',
                'list_filter_sticky',
            )
        }),
        (_('Recent Actions'), {
            'classes': ('wide',),
            'fields': ('recent_actions_visible',)
        }),
    )

    save_on_top = True


admin.site.register(Theme, ThemeAdmin)