from django.conf.urls import url
from userBase.api.views import activateUser

urlpatterns=[
    url("api/activateUser", activateUser.as_view())
]