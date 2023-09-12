from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,CreateView
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

# class HomeView(View):
#     def get(self,request):
#         form=Loginform
#         return render(request,"home.html",{"form":form})

class HomeView(FormView):
    template_name="home.html"
    form_class=Loginform

    def post(self,request,*args,**kwargs):
        form_data=Loginform(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("Username")
            pswd=form_data.cleaned_data.get("Password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"sign in success!!")

                return redirect('custhome')
            else:
                messages.error(request,"sign in faild!!")
                return redirect('h')
        return render(request,"home.html",{"form":form_data})
            

class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')
    
# class RegView(View):
#     def get(self,request):
#         form=RegForm
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"sign up completed!")
#             return redirect("h")
#         return render(request,"reg.html",{"form":form_data})