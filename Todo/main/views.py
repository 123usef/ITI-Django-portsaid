from django.shortcuts import render

#return http response 
from django.http import HttpResponse
#IMPORT MODELS
from .models import Task , Category 

#  Create your views here.

#   Function base view 


def index(request):
    #SELECT * from Task ;
    tasks = Task.objects.all()
    categories = Category.objects.all()

    context = { 'tasks':tasks ,
                'categories' :categories
                }
    # return HttpResponse(tasks)
    return render(request , 'main/index.html',context)




#Class Base View 
