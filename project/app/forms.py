from django import forms
from django.forms import ModelForm
from .models import*

class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        
        fields = ('__all__')

        widgets = {
            
            
           
 
        }