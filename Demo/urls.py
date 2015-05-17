#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from AutoTest.views import *
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$',view=LoginView,name='login'),
	url(r'^logout/$',view=LogoutView,name='logout'),
	url(r'^index/$',view=Index,name='index'),
	url(r'^testcase/$',TestCase,name='testcase'),
	url(r'^changepwd/$',view=ChangepwdView,name='changepwd'),
)