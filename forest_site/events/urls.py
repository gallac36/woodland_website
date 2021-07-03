from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
#to handle images
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

   	path('', views.EventList.as_view(), name='events'),
   	path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),

]

#to handle up loaded images
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
