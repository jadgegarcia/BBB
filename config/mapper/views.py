from django.contrib.auth import logout
from django.db import connection
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm


# Create your views here.


def welcome(request):
    uname = request.session['username']

    if not uname:
        # Handle the case where uname is an empty string
        return redirect('/signin/')
    #return render(request, self.template, {'uname': uname})
    return render(request, "basics/welcome.html", {'uname': uname})


class UserSignUp(View):
    template = 'basics/signup.html'

    def get(self,request):
        form = UserForm()
        return render(request, self.template,{'form':form})

    def post(self,request):
        name = request.POST['username']
        pas = request.POST['password']
        first = request.POST['firstname']
        last = request.POST['lastname']
        occup = request.POST['occupation']
        res = ""
        print(name)
        cursor = connection.cursor()
        args = [name, pas, first, last, occup]
        cursor.callproc('createUser', args)
        result = cursor.fetchall()
        msg = result[0][0]
        cursor.close()
        return render(request, self.template, {'msg':msg})

class UserSignIn(View):
    template = 'basics/signin.html'

    def get(self,request):
        return render(request, self.template)

    def post(self,request):
        name = request.POST['username']
        pas = request.POST['password']
        cursor = connection.cursor()
        args = [name, pas]
        cursor.callproc('checkUser', args)
        result = cursor.fetchall()
        cursor.close()
        if (result[0][0] == 0):
            msg = 'Invalid Credentials'
            return render(request, self.template, {'msg':msg})
        else:
            request.session['username'] = name
            return HttpResponseRedirect('/base/')



class Base(View):
    template = "basics/welcome.html"

    def get(self, request):
        try:
             a = request.session['username']
        except:
            return HttpResponseRedirect('/signin/')


        uname = request.session['username']

        if not uname:
            # Handle the case where uname is an empty string
            return redirect('/signin/')
        return render(request, self.template, {'uname':uname})
class signout(View):

    def get(self, request):
        request.session.clear()
        return HttpResponseRedirect('/signin/')