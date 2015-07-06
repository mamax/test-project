"""productdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from products.views import ProductUpdateView

urlpatterns = [

    url(r'^$', 'products.views.home', name='home'),

    # Products urls
    url(r'^products/$', 'products.views.products_list', name='products'),
    url(r'^products/add$', 'products.views.products_add', name='products_add'),
    url(r'^products/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='products_edit'),

    url(r'^admin/', include(admin.site.urls)),

]
