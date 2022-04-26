from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

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
