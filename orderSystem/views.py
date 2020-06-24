from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render,redirect

def index (request):
    if request.user.is_authenticated:
       return redirect("appindex")
    return render(request,'home/index.html')

@login_required(login_url='/accounts/login/')
def appIndex(request):
    return render(request,'home/appindex.html')