from django.conf.urls import *
from django.contrib import admin, messages
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.urls import path, reverse
from django.utils.html import format_html

from base.models import BaseModel
from orderManagement.models import Order, OrderStatus, OpenOrder, ExecutedOrder, ClosedOrder, LimitOrderPending
from orderManagement.utils import otp_hash
from userBase.models import NormalUser
from vendorbase.models import Symbol, Vendor, Group, City, GlobalPremium, Favourite, VendorDetails


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    change_list_template = 'market_data_table.html'
    def get_queryset(self, request):
        qs = super(SymbolAdmin,self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(vendor_id__user_id=request.user)
        else:
            return qs
    list_display = ('name','vendor_id','buy_premium','sell_premium','enabled')
    list_display_links = ('name',)
    list_filter = ('vendor_id','name')
    list_editable = ('enabled','buy_premium','sell_premium')
    list_per_page = 10
    search_fields = ('name',)

    def changelist_view(self, request, extra_context=None):
        response = super(SymbolAdmin,self).changelist_view(
            request,
            extra_context=extra_context,
        )
        return response

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','city','enabled')
    list_display_links = ('name',)
    list_editable = ('enabled',)
    list_filter = ('city',)
    list_per_page = 10
    readonly_fields = ('vendor_id','margin_available')
    search_fields = ('name','city',)

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return self.readonly_fields
    pass


class OrderAdminBase():
    class Meta:
        pass

def get_vendor_order_queryset(request=None,queryset=None):
    if (request.user.is_superuser):
        return queryset
    else:
        return queryset.filter(instrument_id__vendor_id__user_id=request.user)


@admin.register(LimitOrderPending)
class LimitOrderPendingAdmin(admin.ModelAdmin,OrderAdminBase):
    def get_queryset(self, request):
        return get_vendor_order_queryset(request=request,queryset=self.model.objects.filter(status=OrderStatus.WAITING_FOR_LIMIT))
    list_display = ('instrument_id', 'side', 'quantity', 'status', 'created_at')
    list_display_links = ('instrument_id',)
    list_editable = ('status',)
    list_filter = ('status',)
    list_per_page = 10
    ordering = ('created_at',)
    search_fields = ('order_id', 'instrument_id__name', 'user_id__name')


@admin.register(OpenOrder)
class OpenOrderAdmin(admin.ModelAdmin,OrderAdminBase):
    # def user_id_url(self, obj):
    #     if obj and obj.user_id:
    #         return format_html('<a  href="{}">{}</a>'.format(obj.user_id.get_admin_url(), obj.user_id))
    #
    # user_id_url.make_safe = True
    # user_id_url.allow_tags = True

    def get_urls(self):
        urls = super(OpenOrderAdmin,self).get_urls()
        my_urls = [
            url(r'(?P<order_id>.+?)/confirm_payment/', self.confirm_payment),
        ]
        return my_urls+urls

    def confirm_payment(self,request,order_id):
        order=Order.objects.filter(order_id=order_id).first()
        order.status=OrderStatus.EXECUTED
        order.save()
        #     obj.status=OrderStatus.EXECUTED
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    def approve_payment(self,obj):
        if obj and obj.status:
            return format_html('<a class ="button" href="{}">{}</a>'.format(f"{obj.order_id}/confirm_payment","Confirm Payment"))
    def get_queryset(self, request):
        return get_vendor_order_queryset(request=request,queryset=self.model.objects.filter(status=OrderStatus.OPEN))
    list_display = ('instrument_id' ,'side','quantity','created_at','approve_payment')
    list_display_links = ('instrument_id',)
    list_filter = ('instrument_id__name',)
    list_per_page = 10
    search_fields = ('order_id', 'instrument_id__name', 'user_id__name')


@admin.register(ExecutedOrder)
class ExecutedOrderAdmin(admin.ModelAdmin,OrderAdminBase):

    def get_urls(self):
        urls = super(ExecutedOrderAdmin,self).get_urls()
        my_urls = [
            url(r'(?P<order_id>.+?)/(?P<otp>.+?)/verify_otp/', self.verify_otp),
        ]
        return my_urls+urls

    def verify_otp(self,request,otp,order_id):
        if(str(otp)==str(otp_hash(order_id))):
            Order.objects.filter(order_id=order_id).update(status=OrderStatus.CLOSED)
        else:
            messages.error(request,"INCORRECT OTP")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def user_id_url(self, obj):
        if obj and obj.user_id:
            return format_html('<a href="{}">{}</a>'.format(obj.user_id.get_admin_url(), obj.user_id))
    user_id_url.make_safe = True
    user_id_url.allow_tags = True

    def get_queryset(self, request):
        return get_vendor_order_queryset(request=request,queryset=self.model.objects.filter(status=OrderStatus.EXECUTED))
    # list_display = ('instrument_id', 'user_id_url','side', 'quantity','status','created_at')
    list_display = ('instrument_id','side', 'quantity','status','otp','created_at')
    list_per_page = 10
    search_fields = ('order_id', 'instrument_id__name', 'user_id__username')

    def otp(self,obj):
        return render_to_string('otp_form_item.html', {'order_id':obj.order_id}) #format_html('<input type="text" id="otp" style="width:40px" /> <a class ="button" href="document.getElementById("otp").value;/{}">OK</a></a>'.format(f"{obj.order_id}/verify_otp"))

    list_display_links = ('instrument_id',)
    list_filter = ('status',)

@admin.register(ClosedOrder)
class ClosedOrderAdmin(admin.ModelAdmin,OrderAdminBase):
    def user_id_url(self, obj):
        if obj and obj.user_id:
            return format_html('<a href="{}">{}</a>'.format(obj.user_id.get_admin_url(), obj.user_id))
    user_id_url.make_safe = True
    user_id_url.allow_tags = True
    def get_queryset(self, request):
        queryset = self.model.objects.filter(status=OrderStatus.CLOSED)
        return get_vendor_order_queryset(request=request,queryset=queryset)
           # list_display = ('instrument_id', 'user_id_url','side', 'quantity','status','created_at')
    list_display = ('instrument_id','side', 'quantity','status','created_at')
    list_display_links = ('instrument_id',)
    list_filter = ('status',)
    list_per_page = 10
    search_fields = ('order_id', 'instrument_id__name', 'user_id__name')


@admin.register(Group)
class Group(admin.ModelAdmin):
    pass

@admin.register(City)
class City(admin.ModelAdmin):
    pass

@admin.register(GlobalPremium)
class GlobalPremium(admin.ModelAdmin):
    pass

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    pass
# class OrderEngine_Pool(BaseModel):
#
#     pass

@admin.register(VendorDetails)
class VendorDetailAdmin(admin.ModelAdmin):
    pass
# @admin.register(OrderEngine_Pool)
# class OrderEngineAdmin(admin.ModelAdmin):
#     change_list_template = "StartOrderEngine.html"
#     def get_urls(self):
#         urls = super(OrderEngineAdmin, self).get_urls()
#         my_urls = [url(r"^startOrderEngine/$",startOrderEngine)]
#         return my_urls + urls
