from django import forms
#from django.contrib.authApp.models import User
from domain.models import User
from django.forms import EmailInput, PasswordInput, TextInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_email']
        widgets = {'user_email': TextInput(attrs={'class': "form-control", 'placeholder': "Название задачи"})}

class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {'password': TextInput(attrs={'class': "form-control", 'placeholder': "Название задачи"})}