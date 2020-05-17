from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from . import views
# Import static if not imported
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'saveInfo', views.saveInfo,name='saveInfo'),
    ]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
