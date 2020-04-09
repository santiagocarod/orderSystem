from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class signUp(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        data = {'signUp': form}
        return render(request, 'accounts/signup.html', data)

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("appindex")
        else:
            data = {'signUp': form}
            return render(request, 'accounts/signup.html', data)


class login_v(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        data = {'login': form}
        return render(request, 'accounts/login.html', data)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("appindex")
        else:
            data = {'login': form}
            return render(request, 'accounts/login.html', data)


class logout_v(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("index")
