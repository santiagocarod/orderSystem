from django import forms
from .models import *

class newSupplyForm(forms.ModelForm):

    class Meta:
        model = Supply
        fields=['name','cost','description','quantity']
