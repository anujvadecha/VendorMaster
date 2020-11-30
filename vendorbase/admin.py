from django.conf.urls import *
from django.contrib import admin
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import format_html

from base.models import BaseModel
from orderManagement.models import Order, OrderStatus, OpenOrder, ExecutedOrder, ClosedOrder, LimitOrderPending
from userBase.models import NormalUser
from vendorbase.models import Symbol, Vendor, Group, City, GlobalPremium


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    change_list_template = 'market_data_table.html'
    def get_queryset(self, request):
        qs = super(SymbolAdmin,self).get_queryset(request)
        if not request.user.is_superuser:
            vendor=Vendor.objects.filter(name=request.user.username)[0]
            return qs.filter(vendor_id=vendor)
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
    readonly_fields = ('vendor_id',)
    search_fields = ('name','city',)
    pass

@admin.register(LimitOrderPending)
class LimitOrderPendingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.objects.filter(status=OrderStatus.WAITING_FOR_LIMIT)
    list_display = ('instrument_id', 'side', 'quantity', 'status', 'created_at')
    list_display_links = ('instrument_id',)
    list_editable = ('status',)
    list_filter = ('status',)
    search_fields = ('order_id', 'instrument_id__name', 'user_id__name')
    list_per_page = 10
    ordering = ('created_at',)



@admin.register(OpenOrder)
class OpenOrderAdmin(admin.ModelAdmin):
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
        order=Order.objects.filter(order_id=order_id)
        order.update(status=OrderStatus.EXECUTED)
        #     obj.status=OrderStatus.EXECUTED
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def approve_payment(self,obj):
        if obj and obj.status:
            return format_html('<a class ="button" href="{}">{}</a>'.format(f"{obj.order_id}/confirm_payment","Confirm Payment"))

    def get_queryset(self, request):
        return self.model.objects.filter(status=OrderStatus.OPEN)

    # 'user_id_url'
    list_display = ('instrument_id' ,'side','quantity','created_at','approve_payment')
    list_display_links = ('instrument_id',)
    # list_editable = ( 'status',)
    list_filter = ('instrument_id__name',)
    search_fields = ('order_id', 'instrument_id__name','user_id__name')
    list_per_page = 10

@admin.register(ExecutedOrder)
class ExecutedOrderAdmin(admin.ModelAdmin):
    def user_id_url(self, obj):
        if obj and obj.user_id:
            return format_html('<a href="{}">{}</a>'.format(obj.user_id.get_admin_url(), obj.user_id))
    user_id_url.make_safe = True
    user_id_url.allow_tags = True
    def get_queryset(self, request):
        return self.model.objects.filter(status=OrderStatus.EXECUTED)
    list_display = ('instrument_id', 'user_id_url','side', 'quantity','status','created_at')
    list_display_links = ('instrument_id',)
    list_editable = ( 'status',)
    list_filter = ('status',)
    search_fields = ('order_id',  'instrument_id__name','user_id__name')
    list_per_page = 10

@admin.register(ClosedOrder)
class ExecutedOrderAdmin(admin.ModelAdmin):
    def user_id_url(self, obj):
        if obj and obj.user_id:
            return format_html('<a href="{}">{}</a>'.format(obj.user_id.get_admin_url(), obj.user_id))
    user_id_url.make_safe = True
    user_id_url.allow_tags = True
    def get_queryset(self, request):
        return self.model.objects.filter(status=OrderStatus.CLOSED)
    list_display = ('instrument_id', 'user_id_url','side', 'quantity','status','created_at')
    list_display_links = ('instrument_id',)
    list_editable = ( 'status',)
    list_filter = ('status',)
    search_fields = ('order_id', 'instrument_id__name','user_id__name')
    list_per_page = 10

@admin.register(Group)
class Group(admin.ModelAdmin):
    pass

@admin.register(City)
class City(admin.ModelAdmin):
    pass

@admin.register(GlobalPremium)
class GlobalPremium(admin.ModelAdmin):
    pass


# class OrderEngine_Pool(BaseModel):
#
#     pass

# @admin.register(OrderEngine_Pool)
# class OrderEngineAdmin(admin.ModelAdmin):
#     change_list_template = "StartOrderEngine.html"
#     def get_urls(self):
#         urls = super(OrderEngineAdmin, self).get_urls()
#         my_urls = [url(r"^startOrderEngine/$",startOrderEngine)]
#         return my_urls + urls
