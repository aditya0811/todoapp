# TODO APP

## Softwares Required
This project is about creating a REST API using django, postgres and implementing CRUD operations. I have not used any frontend technologies instead used POSTMAN software for sending requests.

For using this api you have to install following softwares
1. [Python](https://www.python.org/)
2. [VSCode](https://code.visualstudio.com/)-You can use any other editor
3. [Postman](https://www.postman.com/)- If you have experience with frontend technologies you can integrate it, but here I used postman just to check whether our API is working      fine or not.
4. [Postgres](https://www.postgresql.org/)- I used Postgres Database, you can use any other Relational Database.
5. [pgadmin](https://www.pgadmin.org/)- It is a Database Management system for postgres.


## Libraries Required
Following are the libraries that you would require

```
pip install virtualenvwrapper-win
pip install django
pip install psycopg2
```
- [x] Creating a virtual Environement
- [x] Setting up an app
- [x] Object-Realtional Mapper
- [x] Setting up urls and views

## Creating a virtual Environment

Before understanding how Django works it is important to understand why are we creating a virtual environment. Creating a virtual environement is another way of having a completely independent system unrelated to the versison of libraries that are previously installed in our computer. It helps us to deploy projects in isolation.
We can create a virtual environment myfirstvenv using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) assuming you have already installed python and [pip manager](https://pypi.org/project/pip-manager/):-
```
mkvirtualenv workon myfirstvenv
```
To activate myfirstenv
```
myfirstvenv\Scripts\activate
```
To deactivate it
```
deactivate
```

## Setting up an app

Use console to make `todos` app
```
python manage.py startapp todos
```
After this you have to add `todos` inside `INSTALLED_APPS` under settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     #adding application here
    'todos'
]
```

## Object-Realtional Mapper
Django uses the concept of Object-Relational Mapper where using Python we make SQL queries. Here by adding following class we are creating a `Todo` Schema in our database with `content` as an attribute. Below we are importing models which will help us to create a table and specify its column name along with many other options of giving a `default` value or make it compulsory for a user to enter that value using `blank=false` argument.

```
from django.db import models
class Todo(models.Model):
    content =models.TextField()
```

Finally we have to tell django that we have made changes in our schema. We always use below commands whenever we are making changes in our schema.
```
python manage.py makemigrations
python manage.py migrate
```

## Setting up urls and views
Before diving into below code, we have to know what are `views`. Python allows us to define views that handle specific request and return a response whenever following urls are hit. 
We have here three urls(all should be distinct), every url corresponds to a view(can be same or different). 
```
from django.urls import path
from . import views

urlpatterns =[
    path('list/',views.list_todo_items),
    path('insert_todo/',views.insert_todo_item,name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item,name='delete_todo_item'),
]
```


`views.py` handles all the request and response and is basically the heart of our application. The following view helps us to add an object in our database. We are using the POST method to add object to our databse and redirecting a webpage ('/todos/list/') as a response.

```
def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')
```

All thanks to [CodeAffection](https://www.codaffection.com/)

