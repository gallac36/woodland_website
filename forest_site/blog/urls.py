from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

urlpatterns = [

   	#url(r'', views.PostList.as_view(), name='news'),
    path('', views.PostList.as_view(), name='news'),
   	path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
