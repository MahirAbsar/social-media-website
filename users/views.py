from django.shortcuts import render,redirect
from . import views
from  . import forms
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts import forms as pForms

# Create your views here.

def sign_up(request):

    if request.user.is_authenticated:
        return redirect('home')

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
    if request.user.is_authenticated:
        return redirect('home')
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

@login_required(login_url='sign-in')
def sign_out(request):
    logout(request)
    return redirect('sign-in')

@login_required(login_url='sign-in')
def edit_profile(request):
    current_user = models.Profile.objects.get(user=request.user)
    print(current_user)
    form = forms.EditProfileForm(instance=current_user)
    if request.method == "POST":
        form = forms.EditProfileForm(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'users/profile_edit.html',{'form':form})

@login_required(login_url="sign-in")
def info_profile(request):
    form = pForms.PostForm()
    if request.method == "POST":
        form = pForms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            print(post)
    return render(request,'users/profile_info.html',{'form':form})
