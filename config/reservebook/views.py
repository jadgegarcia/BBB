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

            cursor.callproc('reserve_book', [date, username, isbn])
            result = cursor.fetchall()
            cursor.close()
            connection.commit()
            msg = result[0][0]
            big_bad_books = getDetails(isbn)


            try:

                #aaaaaaaaaa
                if 'Reservation successful' == msg:

                    print("SUCCCCCCCCCCCCCCCCCCCESSSSSSSSSSSSSSSSSSSSSSSSSS")
                    #msg = "Reservation successful!"
                    big_bad_books = getBook(request)
                    return render(request, self.template, {"books": big_bad_books, 'uname': username, 'msg': msg})
                else:
                    raise Exception("Error")
            except Exception as e:
                if "Reservation date must be at least 3 weeks from now" == msg:
                    print("SAAAAAAAAAAYOOOOOOOOOO KAAAAAAAAAAAAAAAYOOOOOOOOOOO")
                    #msg = "Failed to reserve this book."
                    print(msg)
                    request.extra_data = ('msg', msg)
                    #return redirect('book:detail', isbn=isbn)
                    return render(request, 'book/detail.html', {"books": big_bad_books, 'uname': username, 'msg': msg})
                else:
                    print("NAKARESEEEEEEEEEEEEEERRRRVEEEEEEEEEEEE")
                    print(msg)
                    #request.extra_data = ('msg', msg)
                    #return redirect('book:detail', isbn=isbn)
                    return render(request, 'book/detail.html', {"books": big_bad_books, 'uname': username, 'msg': msg})




        return redirect('book:books')


def getDetails(isbn):
    cursor = connection.cursor()

    args = [isbn]
    cursor.callproc('GetBookByISBN', args)

    results = cursor.fetchall()
    cursor.close()

    return results


def getBook(request):
    cursor = connection.cursor()

    query = 'SELECT * FROM book_book'
    cursor.execute(query)

    results = cursor.fetchall()
    cursor.close()

    return results


