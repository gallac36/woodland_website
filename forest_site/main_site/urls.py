

from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/', views.index, name='index'),
	#url(r'^events/', views.events, name='events'),
	url(r'^about/', views.about, name='about'),
	url(r'^join/', views.join, name='join'),
	url(r'^firewood/', views.firewood, name='firewood'),
	url(r'^archive/', views.archive, name='archive'),
	url(r'^archivefiles/', views.archivefiles, name='archivefiles'),
]
