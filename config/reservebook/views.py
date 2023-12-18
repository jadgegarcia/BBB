from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
from .forms import ReserveForm

# Create your views here.
class ReserveBook(View):
    template = 'book/books_list.html'

    def get(self, request, isbn):
        try:
            a = request.session['username']
        except:
            return HttpResponseRedirect('/signin/')
        #form = ReserveForm()
        username = request.session['username']

        big_bad_books = getDetails(isbn)

        return render(request, self.template, {"books": big_bad_books, "uname": username, "isbn": isbn})

    def post(self, request, isbn):
        username = request.session['username']
        date = request.POST.get('reservedate')

        with connection.cursor() as cursor:
            try:
                cursor.callproc('reserve_book', [date, username, isbn])
                result = cursor.fetchone()
                cursor.close()
                connection.commit()
                #aaaaaaaaaa
                if result and result[0] == 'Reservation successful':
                    msg = "Reservation successful!"
                    return render(request, self.template, {'msg': msg})
                else:
                    msg = "Failed to reserve this book."
                    return redirect('reservebook:reservebook', isbn=isbn)
            except Exception as e:
                return HttpResponse(f'Error: {str(e)}')



        return redirect('book:books')


def getDetails(isbn):
    cursor = connection.cursor()

    args = [isbn]
    cursor.callproc('GetBookByISBN', args)

    results = cursor.fetchall()
    cursor.close()

    return results