from django.conf.urls import url
from django.contrib import admin

from orderManagement.api.views import placeOrder, getOrderDetails, OrderView

urlpatterns = [
    url("api/placeOrder" , placeOrder),
    url("api/orderDetails" , getOrderDetails),
    url("api/orders" , OrderView.as_view())
]
