from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.db import connection
# Create your views here.
from .forms import BookRequestForm
class RequestView(View):
    template = 'request/request.html'

    def get(self,request):
        try:
            a = request.session['username']
        except:
            return HttpResponseRedirect('/signin/')
        form = BookRequestForm()
        uname = request.session['username']
        results = getRequest(request)
        return render(request, self.template,{'uname':uname, 'results':results, 'form':form})

    def post(self, request):
        name = request.session['username']
        title = request.POST['booktitle']
        author = request.POST['bookauthor']
        publisher = request.POST['bookpublisher']
        date = request.POST['bookdate']
        req = request.POST['requestdate']
        res = ""
        print(title)
        cursor = connection.cursor()
        args = [name, title, author, publisher, date, req, res]
        cursor.callproc('createRequest', args)
        result = cursor.fetchall()
        msg = result[0][0]



        results = getRequest(request)
        cursor.close()
        return render(request, self.template, {'msg':msg, 'results':results, 'uname': request.session['username'], 'form':BookRequestForm()})

class RequestList(View):
    template = 'request/request_list.html'

    def get(self,request):

        results = getRequest(request)
        return render(request, self.template, {'results': results})




def getRequest(request):
    cursor = connection.cursor()
    query = 'select * from requestbook_requestbook'
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close

    return results