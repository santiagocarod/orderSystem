from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class productIndex(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        data = {'products':products}
        return render(request, 'products/index.html',data)

@method_decorator(login_required,name='dispatch')
class newProduct(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required,name='dispatch')
class editProduct(View):
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        pass


@method_decorator(login_required,name='dispatch')
class deleteProduct(View):
    def post(self, request, *args, **kwargs):
        pass