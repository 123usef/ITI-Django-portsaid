from django.db import models

# Create your models here.
class Project(models.Model):
    # id = By Default any Entity(Class ) Django orm will add the Id By Default 
    name = models.CharField(max_length = 150 , null = False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null = True)
