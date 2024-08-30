from django.shortcuts import render

#return http response 
from django.http import HttpResponse
#IMPORT MODELS
from .models import Task , Category 

#  Create your views here.

#   Function base view 


def index(request):
    #SELECT * from Task ;
    tasks = Task.objects.all().order_by('due_date')
    # tasks = Task.objects.filter(status ='PENDING' )
    categories = Category.objects.all()

    context = { 'tasks':tasks ,
                'categories' :categories
              }
    # return HttpResponse(tasks)
    return render(request , 'main/index.html',context)


def detailed_task(request ,id):
    task = Task.objects.get(id=id)
    context = {
        'task':task
    }
    return render(request , 'main/detailed.html' , context)
#Class Base View 

def todo_by_status(request , st):
    todos = Task.objects.filter(status = st)
    context = {
        'todos' :todos
    }
    return render(request , 'main/todosstatus.html' , context)