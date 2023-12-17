from django.shortcuts import render

# Create your views here.
from django.db import connection
from django.db.models import OuterRef, Subquery
from django.forms import ModelForm
from django.shortcuts import render
from django.views import View


# Create your views here.


class ReturnList(View):
    def get(self, request):
        username = request.session['username']




        """with connection.cursor() as cursor:
            # Call the GetReturnedBooks procedure
            cursor.execute("CALL GetReturnedBooks(%s)", [username])
            returned_books = cursor.fetchall()

            # Call the GetUnreturnedBooks procedure
            cursor.execute("CALL GetUnreturnedBooks(%s)", [username])
            unreturned_books = cursor.fetchall()

        context = {
            'username': username,
            'borrowed_books': unreturned_books,
            'returned_books': returned_books,
        }"""
        cursor = connection.cursor()
        args = [username]
        cursor.callproc('GetBorrowedBooksByUser', args)
        results = cursor.fetchall()
        cursor.close()
        # return redirect('donation')



        return render(request, "return/returnbook.html", {'results': results, 'uname':username})

class ReturnBook(View):

    def get(self, request, isbn):
        uname = request.session['username']  # Assuming 'username' is passed as an argument

        return render(request, 'return/returnbook.html', {'uname': uname})