from django.conf.urls import url
from userBase.api.views import ActivateUser

urlpatterns=[
    url("api/activateUser", ActivateUser.as_view())
]