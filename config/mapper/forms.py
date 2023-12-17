from django import forms
from django.forms import ModelForm, TextInput, PasswordInput
from account.models import User


class UserForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    occupation = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = User
        fields = '__all__'