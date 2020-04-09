from django.conf.urls import url, include
from django.contrib import admin
from . import views as accountViews

app_name ='accounts'

urlpatterns = [
    url(r'^signUp/',accountViews.signUp.as_view(),name='signUp'),
    url(r'^login/',accountViews.login.as_view(),name='login'),
]
