"""orderSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views as orderViews

app_name ='orderSystem'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',orderViews.index,name='index'),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^app/',orderViews.appIndex,name='appindex'),
    url(r'^supplies/',include('supplies.urls',namespace='supplies')),
    url(r'^products/',include('products.urls',namespace='products')),
]
