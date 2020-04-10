from django.conf.urls import url, include
from django.contrib import admin
from . import views as suppliesViews

app_name = 'supplies'

urlpatterns = [
    url(r'^$', suppliesViews.supplyIndex.as_view(),name='suppliesIndex'),
    url(r'^newSupply/',suppliesViews.newSupply.as_view(),name='newSupply'),
]
