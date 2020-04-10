from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import newSupplyForm
from .models import supply
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name='dispatch')
class newSupply(View):
    def get(self, request, *args, **kwargs):
        form = newSupplyForm()
        data = {'form': form}
        return render(request, 'supplies/newSupply.html',data)
    def post(self, request, *args, **kwargs):
        form = newSupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appindex')
        else:
            data = {'form': form}
            return render(request, 'supplies/newSupply.html',data)

@method_decorator(login_required,name='dispatch')
class supplyIndex(View):
    def get(self, request, *args, **kwargs):
        supplies = supply.objects.all()
        data = {'supplies':supplies}
        return render(request, 'supplies/index.html',data)
