from django.conf.urls import url, include
from django.contrib import admin
from . import views as accountViews

app_name = 'accounts'

urlpatterns = [
    url('signUp/', accountViews.signUp.as_view(), name='signUp'),
    url('login/', accountViews.login_v.as_view(), name='login'),
    url('logout/', accountViews.logout_v.as_view(), name='logout'),
]
