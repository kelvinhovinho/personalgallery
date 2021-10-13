from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    re_path('location/(?p<location>\w+)',views.location,name = 'location'),
    path('search/', views.search_results, name='search_results')
 ]


if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)