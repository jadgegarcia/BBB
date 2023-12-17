from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Book, BigBadBook


# Create your views here.
class Books(View):
    template = "book/books_list.html"

    def get(self, request):
        try:
            username = request.session['username']
        except:
            return HttpResponseRedirect('/login')

        print("Inside books username: " + username)
        big_bad_books = getBook(request)
        return render(request, self.template, {"books": big_bad_books, 'uname': username})


class Detail(View):
    template = "book/detail.html"

    def get(self, request, isbn):  # Include the 'isbn' parameter in the GET method
        try:
            username = request.session['username']
        except KeyError:
            return HttpResponseRedirect('/login')

        print("Inside detail username:" + username)



        big_bad_books = getDetails(isbn)
        #big_bad_books = get_object_or_404(BigBadBook, isbn=isbn)

        return render(request, self.template, {"books": big_bad_books, "uname": username, "isbn": isbn})





def getBook(request):
    cursor = connection.cursor()

    query = 'SELECT * FROM book_book'
    cursor.execute(query)

    results = cursor.fetchall()
    cursor.close()

    return results


def getDetails(isbn):
    cursor = connection.cursor()

    args = [isbn]
    cursor.callproc('GetBookByISBN', args)

    results = cursor.fetchall()
    cursor.close()

    return results

