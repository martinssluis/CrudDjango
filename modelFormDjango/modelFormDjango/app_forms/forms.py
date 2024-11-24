from django import forms
from .models import Client
from django.forms import DateInput

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'dt_birth', 'sex', 'email']
        widgets = {
            'dt_birth': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
