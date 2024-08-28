from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #manuipulate the request 

    #return template 
    # return render()
    return HttpResponse("hello world from django ")