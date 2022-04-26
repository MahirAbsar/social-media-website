from django.shortcuts import render,redirect
from . import views
from . import forms
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def sign_up(request):
    page = 'sign_up'
    form = forms.CreateUserForm()
    if request.method=="POST":
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            user_profile =models.Profile(user = user)
            user_profile.save()
            return redirect('home')
    return render(request,'users/login_register.html',{'title':'Sign Up','form':form,'page':page})

def sign_in(request):
    form = forms.UserSignInForm()
    if request.method == 'POST':
        form = forms.UserSignInForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('No User Exists')
            return redirect('sign-in')
        user = authenticate(request, password=password, username=username)
        if user:
            login(request, user)
            print("here")
            return redirect('home')
        else:
            print("User Credentials Wrong")

    return render(request,'users/login_register.html',{'title':'Sign In','form':form})

def sign_out(request):
    logout(request)
    return redirect('sign-in')
