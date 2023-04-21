from django.contrib.auth.forms import UserCreationForm
from .models import Customusers
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class custom_usercreation_form(UserCreationForm):
    email=forms.EmailField(required=True)
    profile_pic=forms.ImageField(required=False)
    user_type=forms.ChoiceField(choices=(('patient','Patient'),('doctor','Doctor')),widget=forms.RadioSelect(),required=True)
    address_line1=forms.CharField(max_length=1000,required=False)
    city=forms.CharField(max_length=50,required=False)
    state=forms.CharField(max_length=50,required=False)
    pincode=forms.CharField(max_length=6,required=False)
    
    
    
    class Meta:
        model=Customusers
        fields=('user_type','first_name','last_name','username','email','password1','password2','address_line1','city','state','pincode')

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'})