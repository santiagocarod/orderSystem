from django.conf.urls import url, include
from django.contrib import admin
from . import views as productsViews

app_name = 'Products'

urlpatterns = [
    url(r'^$', productsViews.productIndex.as_view(),name='productsIndex'),
    url(r'^newProduct/',productsViews.newProduct.as_view(),name='newProduct'),
    url(r'^deleteProduct/',productsViews.deleteProduct.as_view(),name='deleteProduct'),
    url(r'^editProduct/',productsViews.editProduct.as_view(),name='editProduct'),
]
