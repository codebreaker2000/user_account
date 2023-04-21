from django.shortcuts import render,redirect
from .forms import custom_usercreation_form,LoginForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from .models import Customusers


# Create your views here.

def index(request):
    return render(request,"users/index.html")

def Register(request):
    if request.method=="POST":
        forms=custom_usercreation_form(request.POST,request.FILES)
        if forms.is_valid():

            user=forms.save(commit=False)
            user.is_patient=(forms.cleaned_data.get('user_type')=='patient')
            user.is_doctor=(forms.cleaned_data.get('user_type')=='doctor')
            user.save()
            return redirect("login")
        
        
    else:
        forms=custom_usercreation_form()   
    return render(request,"users/register.html",{'forms':forms})  

def Login(request):
    if request.method=="POST":
        
        forms=LoginForm(request=request, data=request.POST)
        
        if forms.is_valid():
           
            username=forms.cleaned_data.get('username')
            password=forms.cleaned_data.get('password')
            user=authenticate(request=request,username=username,password=password)
            if user is not None:
                
                login(request,user)
                if user.is_patient:
                    print("yes")
                    user_data = Customusers.objects.filter(username=request.user.username).first()

                    return render(request,'users/patient.html',{'user_data':user_data})
                elif user.is_doctor:
                    user_data = Customusers.objects.filter(username=request.user.username).first()
                    print(user_data)
                    return render(request,'users/doctor.html',{'user_data':user_data})
        else:
            print(forms.errors)        
    else:
        forms=LoginForm()
    return render(request,'users/login.html',{'forms':forms}) 
              

        
