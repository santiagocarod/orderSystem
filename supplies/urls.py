from django.conf.urls import url, include
from django.contrib import admin
from . import views as suppliesViews

app_name = 'Supplies'

urlpatterns = [
    url(r'^$', suppliesViews.supplyIndex.as_view(),name='suppliesIndex'),
    url(r'^newSupply/',suppliesViews.newSupply.as_view(),name='newSupply'),
    url(r'^deleteSupply/',suppliesViews.deleteSupply.as_view(),name='deleteSupply'),
    url(r'^editSupply/',suppliesViews.editSupply.as_view(),name='editSupply'),
]
