from django.shortcuts import render, redirect #Para renderizar y redireccionar 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm #Para crear formuario Authe es para comprovar si el usuario existe
from django.contrib.auth.models import User #Para registrar usuarios
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate #Para crear los Cockiers
from django.db import IntegrityError # Para conocer los errores de la base de datos


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
    
def tasks(request):
    return render(request, 'tasks.html')

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
        