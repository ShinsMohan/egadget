from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Loginform(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput())

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]