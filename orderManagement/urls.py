from django.conf.urls import url
from django.contrib import admin

from orderManagement.api.views import placeOrder, getOrderDetails

urlpatterns = [
    url("api/placeOrder",placeOrder),
    url("api/orderDetails",getOrderDetails)
]
