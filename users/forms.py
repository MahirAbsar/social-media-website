from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . import models

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email...'}))
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserSignInForm(AuthenticationForm):
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class EditProfileForm(forms.ModelForm):
    dob = forms.DateTimeField(label="Date of Birth",widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model= models.Profile
        exclude = ['user']
