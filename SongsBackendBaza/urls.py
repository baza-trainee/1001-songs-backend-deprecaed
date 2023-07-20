"""
URL configuration for SongsBackendBaza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django_otp.admin import OTPAdminSite

# admin.site.__class__ = OTPAdminSite

schema_view = get_schema_view(
    openapi.Info(
        title='1001SongsAPI',
        default_version='v1',
        description='About 1001Songs',
        contact=openapi.Contact(email='admin@admin.com')
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth', include('apps.auth.urls')),
    path('songs', include('apps.songs.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
