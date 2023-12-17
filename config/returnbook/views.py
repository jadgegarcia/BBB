from django.db import connection
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
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

    """def post(self, request, username):
        if request.method == 'POST':
            uname = username  # Assuming 'username' is passed as an argument

            borrow_id = request.POST.get('borrow_id')
            condition = request.POST.get('condition')

            with connection.cursor() as cursor:
                args = [borrow_id, uname]
                cursor.callproc('AddToReturnTable', args)
                result = cursor.fetchall()
                msg = result[0][0]
                cursor.execute("CALL GetReturnedBooks(%s)", [username])
                returned_books = cursor.fetchall()
                cursor.execute("CALL GetUnreturnedBooks(%s)", [username])
                unreturned_books = cursor.fetchall()
                context = {
                    'msg': msg,
                    'username': username,
                    'borrowed_books': unreturned_books,
                    'returned_books': returned_books,
                    'uname': request.session['username'],
                }
            return render(request, 'return/returnbook.html', context)"""


class AddReturn(View):

    def get(self, request):
        try:
            username = request.session['username']
        except KeyError:
            return HttpResponseRedirect('/login')
        print("Inside detail username:" + username)

        return render(request, 'return/returnbook.html')



    def post(self, request, borrow_id):
        username = request.session['username']
        print(borrow_id)


        cursor = connection.cursor()
        args = [int(borrow_id), username]

        cursor.callproc('AddToReturnTable', args)
        result = cursor.fetchall()
        msg = result[0][0]
        cursor.close()

        return render(request, 'return/returnbook.html')