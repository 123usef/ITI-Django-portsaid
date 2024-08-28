1-i have to make sure that VirtualEnv is installed
*************************************
virtualenv --version 
no of the version 

if Not Installed :
-----------------
1.1-pip install virtualenv  
----------------------------------
2. Create Virtual Enviroment 

2.1- virtualenv virtualenviromentname
--------------------------------------------
3- activate virtual enviroment :

** bash : source virtualenviromentname/Scripts/activate
(virtualenviromentname)

**cmd(windows) :  virtualenviromentname\Scripts\activate


------------------------------------------------------------------
4- install django using pip  :

pip install django 

--------------------------------------------------------------
5- create Project using django 
django-admin startproject projName 

--------------------------------------------------------------
6- create Application within the Project 

change Directory : cd  projName (manage.py)

python manage.py startapp applicationName 

-------------------------------------------------------------
7-to start the server 
python manage.py runserver 
-------------------------------------- -----------------------
8- Database 
 
**python manage.py makemigrations --> translate userDefined Models to migration to perpare them to be database table's 
**python manage.py migrate -->  apply the Migrations 

------------------------------------------------------------
9- Create Super user in django admin site
 
** python manage.py createsuperuser 
--------------------------------------------------------------------------------------------------
1-your today lab  
-----------------
initialize django project  with one application(main)  the Project will be a todolist has a model Called Todo each todo'
should have  name , description , deadline(dateField )  migrate the Table and register it in admin site .
also you will have to render the "hello world from django"  from main app 









