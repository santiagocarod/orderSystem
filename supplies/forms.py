from django import forms
from .models import supply

class newSupplyForm(forms.ModelForm):

    class Meta:
        model = supply
        fields=['name','cost','description','quantity']
