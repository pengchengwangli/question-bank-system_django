from django.shortcuts import render, redirect
from django.http import HttpResponse


# from django.shortcuts import render

def index(request):
    return redirect('/index/')


def test(request):
    session = request.session
    # request
    print(request.user.password)
    return HttpResponse("ok")
