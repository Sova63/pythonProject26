from django import forms
from domain.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'user_email']
        labels = {
            'username': 'Введите имя',
            'password': 'Введите пароль',
            'user_email': 'Введите email'
        }
        widgets = {
            'username': TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Введите имя"}),
            'password': PasswordInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Введите пароль"}),
            'user_email': EmailInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Введите email"})
        }