from django.db import connection
from django.shortcuts import render
from django.views import View


class ReturnBook(View):
    def get(self, request, username):
        with connection.cursor() as cursor:
            # Call the GetReturnedBooks procedure
            uname = request.session['username']
            cursor.execute("CALL GetReturnedBooks(%s)", [uname])
            returned_books = cursor.fetchall()

            # Call the GetUnreturnedBooks procedure
            cursor.execute("CALL GetUnreturnedBooks(%s)", [uname])
            unreturned_books = cursor.fetchall()

        context = {
            'username': request.session['username'],
            'borrowed_books': unreturned_books,
            'returned_books': returned_books,
            'uname':request.session['username'],
        }
        return render(request, "return/returnbook.html", context)
    def post(self, request, username):
        uname = username
        borrow_id = request.POST.get('borrow_id')

        with connection.cursor() as cursor:
            args = [borrow_id, uname]
            cursor.callproc('AddToReturnTable', args)
            result = cursor.fetchall()
            msg = result[0][0]
            # Call the GetReturnedBooks procedure
            uname = request.session['username']
            cursor.execute("CALL GetReturnedBooks(%s)", [uname])
            returned_books = cursor.fetchall()

            # Call the GetUnreturnedBooks procedure
            cursor.execute("CALL GetUnreturnedBooks(%s)", [uname])
            unreturned_books = cursor.fetchall()

        context = {
            'username': request.session['username'],
            'borrowed_books': unreturned_books,
            'returned_books': returned_books,
            'uname':request.session['username'],
        }
        return render(request, 'return/returnbook.html',context)