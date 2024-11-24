from django import forms
from domain.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField
from django.core.exceptions import ValidationError



class UserForm(forms.ModelForm):
    confirm_password = CharField(
        widget=PasswordInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Повторите пароль"}),
        label=('Повторите пароль'))

    terms_accepted = forms.BooleanField(
        required=True,
        label='Я согласен со всеми положениями <a href="#!" class="text-body"><u>Условий обслуживания</u></a>',
        error_messages={'required': 'Вы должны принять условия обслуживания.'}
    )

    class Meta:
        model = User
        fields = ['username', 'password','user_email']
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Пароли не совпадают.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        #user.password = encrypt_password(user.password)  # Шифруем пароль перед сохранением
        user.save()
        return user




