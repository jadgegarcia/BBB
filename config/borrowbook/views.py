from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class Borrow(View):
    template = 'book/books_list.html'
    def get(self, request, isbn):
        try:
            username = request.session['username']
        except KeyError:
            return HttpResponseRedirect('/login')

        print("Inside detail username:" + username)
        #big_bad_books = get_object_or_404(BigBadBook, isbn=isbn)

        # Cursor connection to execute the stored procedure borrowBook
        cursor = connection.cursor()
        args = [isbn, username]
        cursor.callproc('borrowBook', args)
        result = cursor.fetchall()
        message = result[0][0]
        cursor.close()

        if message == 'Book borrowed successfully.':
            cursor = connection.cursor()
            args = [username]
            cursor.callproc('GetBorrowedBooksByUser', args)
            results = cursor.fetchall()
            cursor.close()
            return redirect('book:books')
            #return render(request, self.template)
            #return render(request, self.template, {"uname": username, "message": message, "isbn": isbn})



        return redirect('borrow:borrow')



