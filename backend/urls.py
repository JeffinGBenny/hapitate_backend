"""mynotes URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    # email links
    path(
        'api/v1/dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path(
        'api/v1/dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),  # Needs to be defined before the registration path
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path(
        'api/v1/rest-auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    # local apps Urls
    path('api/', include('api.urls')),
    path('api/', include('authentication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
