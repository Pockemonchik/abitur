from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    url('login/',views.log,name="log"),
    url('logout/',views.logout_view,name="logout")
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
