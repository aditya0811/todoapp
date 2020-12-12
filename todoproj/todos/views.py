from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def list_todo_items(request):
    #if we were to just return a page showing some mesage we will just comment 11,12 line and add
    #10th line 
    #return HttpResponse('from list_todos_items')
    #Here instead of returning a message we will be returning html pages which are
    #stored in templates in a django project
    context = {'todo_list' : Todo.objects.all()}
    return render(request, 'todos/todo_list.html',context)


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')