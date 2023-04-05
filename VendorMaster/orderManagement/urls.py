from django.conf.urls import url

from orderManagement.api.views import OrderView, UserMarginsView

urlpatterns = [
    url( "api/orders" , OrderView.as_view()),
    url( "api/usermargins" , UserMarginsView.as_view())
]
