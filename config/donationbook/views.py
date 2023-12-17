from django.db import connection
from django.shortcuts import render, redirect
from django.views import View
from .forms import BookDonationForm

# Create your views here.




class donation(View):
    template = 'donationbook/donate.html'

    def get(self, request):
        #return render(request, "donationbook/donate.html")
        form = BookDonationForm()
        uname = request.session['username']
        results = getDonation(request)

        if not uname:
            # Handle the case where uname is an empty string
            return redirect('/signin/')
        return render(request, self.template, {'form': form, 'uname': uname, 'results': results})



class donate_book(View):

    def post(self, request):
        # Check if the form is valid
        uname = request.session['username']
        form = BookDonationForm(request.POST)
        if form.is_valid():
            # Extract form data
            isbn = form.cleaned_data['ISBN']
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']


        # Get the username from the session
        username = request.session.get('username')

        cursor = connection.cursor()
        args = [isbn, title, author, genre, username]
        cursor.callproc('insert_or_update_book', args)


        cursor.close()
        #return redirect('donation')
        results = getDonation(request)

        # Return the template with the form and donated_books
        return render(request, 'donationbook/donate.html', {'form': BookDonationForm(), 'results': results, 'uname':uname})



class DonationList(View):
    template = 'donationbook/donate.html'

    def get(self, request):
        results = getDonation(request)
        return render(request, self.template, {'results': results})


def getDonation(request):
    username = request.session.get('username')
    cursor = connection.cursor()

    query = 'SELECT * FROM displayDonation WHERE customer_id_id = %s'
    cursor.execute(query, [username])

    results = cursor.fetchall()
    cursor.close()

    return results