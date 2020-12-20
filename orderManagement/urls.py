from django.conf.urls import url
from django.contrib import admin

from orderManagement.api.views import placeOrder, getOrderDetails, OrderView, UserMarginsView

urlpatterns = [
    url("api/placeOrder" , placeOrder),
    url("api/orderDetails" , getOrderDetails),
    url("api/orders" , OrderView.as_view()),
    url("api/usermargins" , UserMarginsView.as_view())
]
