from datetime import datetime

from django import forms
from .models import Entry
from django.forms import ModelForm,TextInput,Textarea,DateInput

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [ 'date', 'text']
        labels = {
            'date': 'Дата',
            'text': 'Текст сообщения'
        }
        widgets = {
            'date': DateInput(attrs={'class': "form-control",'type':"date", 'placeholder': "Дата"}),
            'text': Textarea(attrs={'class': "form-control", 'placeholder': "Текст сообщения"})
        }