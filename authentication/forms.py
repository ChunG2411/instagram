from xml.parsers.expat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name']