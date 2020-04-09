from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,update_session_auth_hash


class signUp(View):
    def get(self, request, *args,**kwargs):
        form = UserCreationForm()
        data = {'signUp':form}
        return render(request, 'accounts/signup.html',data)
    
    def post(self, request, *args,**kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        else:
            data = {'signUp':form,'error':form.errors}
            return render(request,'accounts/signup.html',data)



class login(View):
    def get(self, request,*args, **kwargs):
        form = AuthenticationForm()
        data = {'login':form}
        return render(request,'accounts/login.html',data)
    def post(self, request,*args, **kwargs):
        form = AuthenticationForm()
        if form.is_valid():
            user = form.get_user()
            login(request,user)

class logout(View):
    def post(self, request,*args, **kwargs):
        logout(request)

