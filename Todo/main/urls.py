from django.urls import path 
from .views import index

urlpatterns = [
    #patterns for the url / , /products
    path('' , index , name="home")
]
