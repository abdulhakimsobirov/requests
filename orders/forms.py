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
        widgets = {
            'name': forms.TextInput(attrs={'type':"text", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Напишите название объекта"  })
            }


class BrigadirForm(forms.ModelForm):
    class Meta:
        model = Brigadir
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'type':"text", 'class': "form-control", 'id':"formGroupExampleInput", 'placeholder':"Напишите Ф.И.О бригадира"}),
            'phone': forms.TextInput(attrs={'type':"text", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Напишите номер бригадира" }),
            }


class RequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['brigadir', 'object', 'lunch', 'dinner', 'late_dinner']

        widgets = {
            'brigadir': forms.Select(attrs={'type':"text", 'class': "form-control", 'id':"formGroupExampleInput", 'placeholder':"Выберите бригадир"}),
            'object': forms.Select(attrs={'type':"select", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Выберите объект" }),
            'lunch': forms.NumberInput(attrs={'type':"text", 'pattern':"[0-9]", 'class': "form-control", 'id':"formGroupExampleInput3", 'placeholder':"Напишите количество обеда" }),
            'dinner': forms.NumberInput(attrs={'type':"text", 'pattern':"[0-9]", 'class': "form-control", 'id':"formGroupExampleInput4", 'placeholder':"Напишите количество ужина" }),
            'late_dinner': forms.NumberInput(attrs={'type':"text", 'pattern':"[0-9]*", 'class': "form-control", 'id':"formGroupExampleInput5", 'placeholder':"Напишите количество позужина" }),
            }


        

class RequestIsActiveForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['is_active']

        widgets = {
            'is_active': forms.Select(attrs={'type':"select", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Выберите объект" }),
        }

class ObjectIsActiveForm(forms.ModelForm):
    class Meta:
        model = Objects
        fields = ['is_active']

        widgets = {
            'is_active': forms.Select(attrs={'type':"select", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Выберите объект" }),
        }

class BrigadirIsActiveForm(forms.ModelForm):
    class Meta:
        model = Brigadir
        fields = ['is_active']

        widgets = {
            'is_active': forms.Select(attrs={'type':"select", 'class': "form-control", 'id':"formGroupExampleInput2", 'placeholder':"Выберите объект" }),
        }