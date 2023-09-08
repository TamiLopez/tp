from django.shortcuts import render, redirect, get_object_or_404 #Para renderizar y redireccionar 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm #Para crear formuario Authe es para comprovar si el usuario existe
from django.contrib.auth.models import User #Para registrar usuarios
from django.contrib.auth import login, logout, authenticate #Para crear los Cockiers
from django.db import IntegrityError # Para conocer los errores de la base de datos
from tp.settings import TIME_ZONE
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required



def home(request):
    
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # regitro de usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],password=request.POST
                    ['password1'])
                user.save()
                login(request, user)
                return redirect('Tasks') # reinderia a Taks una vez que , como tiene return ya no lee los bloquedes de abajo
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": "Username already exists"
                    })
        return render(request, 'signup.html',{
            'form':UserCreationForm,
            "error": "EL Password no coincide"
        })

@login_required    
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted_isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

@login_required 
def signout(request):
    logout(request)
    return redirect('home')
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm          
    })
    else:
        user = authenticate(
            request, username=request.POST['usename'], pasword=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or password incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')

@login_required 
def create_task(request):
    
    if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form': TaskForm
    })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user 
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html',{
                'form': TaskForm
                'error': "plase provide valida data"
                })


@login_required 
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id)
        form = TaskForm(instance=task) # Para Actualizar la Tareas
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=Task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {
                'task': task,
                'form': form,
                'error': "Error Actualizando Tarea "
            })
            
@login_required           
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datacompleted = timezone.now
        task.save()
        return redirect('tasks')

@login_required 
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required   
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted_isnull=True)
    ('-datecompleted') 
    return render(request, 'tasks.html', {'tasks': tasks})