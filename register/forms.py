from django.core import validators    #------------optional----------------
from django.core import validators
from django import forms
from django.forms import widgets
from .models import Users

class UsersForm(forms.ModelForm ):
    class Meta:
        model = Users
        fields =['first_name','last_name','email','password',]
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
                    
        }
