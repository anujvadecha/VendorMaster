"""VendorMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from VendorMaster import settings
from vendorbase.api.views import get_normalUser, UserValidationView

urlpatterns = [
    url('admin/', admin.site.urls),
    url('order/', include("orderManagement.urls")),
    url('api/', include("api.urls")),
    path('api-auth/', include("rest_framework.urls")),
    path("api/rest-auth/",include("rest_auth.urls")),
    path("api/rest-auth/registration",include("rest_auth.registration.urls")),
    path("api/normaluser",UserValidationView.as_view())
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)