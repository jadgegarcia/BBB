from django.forms import ModelForm
from django import forms
from .models import ReserveBook

class ReserveForm(ModelForm):
    reservation_date = forms.DateField(label='reservedate', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'ex. MM - DD - YYYY'}))

    class Meta:
        model = ReserveBook
        fields = ['reservation_date']