
from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',include('main.url')),
    path('database/', include('datab_app.urls')),
    path('users/', include('users.urls')),
]
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)