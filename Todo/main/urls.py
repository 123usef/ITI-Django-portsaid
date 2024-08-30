from django.urls import path 
from .views import index , detailed_task , todo_by_status

urlpatterns = [
    #patterns for the url / , /products
    path('' , index , name="home"),
    path('detailed/<int:id>' , detailed_task , name ="detail"),
    path('todos/status/<str:st>' , todo_by_status , name ="status")
]
