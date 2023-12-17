from django.forms import ModelForm
from django import forms
from .models import RequestBook

class RequestForm(ModelForm):
    book_title = forms.CharField(widget=forms.TextInput)
    request_date = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = RequestBook
        fields = ['book_title', 'request_date']




class BookRequestForm(forms.Form):
    booktitle = forms.CharField(label='Book Title', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. One Piece'}))
    bookauthor = forms.CharField(label='Book Author', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Eiichiro Oda'}))
    bookpublisher = forms.CharField(label='Book Publisher', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Shueisha'}))
    bookdate = forms.DateField(label='Book Publish Date', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. MM - DD - YYYY'}))
    requestdate = forms.DateField(label='Request Date', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. MM - DD - YYYY'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize the labels, help_texts, etc. here if needed
        self.fields['bookdate'].input_formats = ['%m - %d - %Y']
        self.fields['requestdate'].input_formats = ['%m - %d - %Y']