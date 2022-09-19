from dataclasses import field, fields
from django import forms
from .models import Requests, Objects, Brigadir
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class ObjectsForm(forms.ModelForm):
    class Meta:
        model = Objects
        fields = ['name']


class BrigadirForm(forms.ModelForm):
    class Meta:
        model = Brigadir
        fields = ['name', 'phone']


class RequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['brigadir', 'object', 'lunch', 'dinner', 'late_dinner']