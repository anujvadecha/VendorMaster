"""
VendorMaster URL Configuration
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

import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.core.cache import cache
from django.urls import include, path, re_path
from VendorMaster import settings
from userBase.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView
from vendorbase.api.views import FavouritesView
from vendorbase.models import Symbol
from vendorbase.views import IndexTemplateView, fallback_404

# Symbol.update_cache()
urlpatterns = [
    url('admin/', admin.site.urls),
    url('order/', include("orderManagement.urls")),
    path("accounts/register/", RegistrationView.as_view(
        form_class=CustomUserForm,
        success_url="/",
    ),name="django_registration_register"),
    path('accounts/',include('allauth.urls')),
    # path("accounts/",include("django_registration.backends.one_step.urls")),
    path("accounts/",include("django.contrib.auth.urls")),
    url('api/', include("api.urls")),
    path('api-auth/', include("rest_framework.urls")),
    path("api/rest-auth/",include("rest_auth.urls")),
    path("api/rest-auth/registration",include("rest_auth.registration.urls")),
    path("",IndexTemplateView.as_view(),name="entry-point"),
    path("api/favourites/",FavouritesView.as_view(),name="favourite"),
    url(r'^.*$',fallback_404,name="404 fallback")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)