from django.urls import path
from api.views import (
    UserRegisterView
)

app_name = "api"

urlpatterns = [
    # path('register/', UserRegisterView, name="register"),
]