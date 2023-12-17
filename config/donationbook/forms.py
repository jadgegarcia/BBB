from django import forms
from book.models import Book
class BookDonationForm(forms.Form):
    ISBN = forms.CharField(label='ISBN', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN (required)'}))
    title = forms.CharField(label='Title', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title (required)'}))
    author = forms.CharField(label='Author', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author (required)'}))
    genre = forms.CharField(label='Genre', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre (required)'}))
    #description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}))

    # You can add more fields as needed

    def clean_ISBN(self):
        isbn = self.cleaned_data.get('ISBN')
        # Add validation logic for ISBN if needed
        return isbn

    class Meta:
        model = Book
        fields = ('ISBN', 'title', 'author', 'email', 'genre', 'is_donated')