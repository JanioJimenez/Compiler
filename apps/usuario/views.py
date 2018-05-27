from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core import serializers

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User #Usuario Django por defecto
from django.contrib.auth.forms import UserCreationForm

from apps.usuario.models import Usuario #Usuario (comunidad)
from apps.usuario.forms import UsuarioForm, RegistroForm

from django.views.generic import CreateView

from django.contrib import messages
import json

# Create your views here.

def index(request):
    context = {"mensaje":"hola"}
    return render(request,'index.html', context)

def usuario(request):
    context = {"mensaje":"hola"}
    return render(request,'usuario.html', context)

def registro(request):
    print('Llegue al servidor')

    first_name =''
    last_name=''
    email=''
    username=''
    password=''
    edad=''
    ciudad=''
    pais=''
    lenguaje=''

    respuesta = 0 

    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST.get('password')
        edad = request.POST['edad']
        ciudad  = request.POST['ciudad']
        pais = request.POST['pais']
        lenguaje  = request.POST['lenguaje']

        
        objeto = User.objects.filter(username = username, email = email)

        if objeto : #Si (list_message != Vacia): return (False), No es vacia (True)
            print("Don D")
            respuesta = 1
        else:
            respuesta = 2
            user = User.objects.create_user(username, email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

            usuario = Usuario(edad = edad, ciudad = ciudad, pais = pais, 
            lenguaje = lenguaje, usuario_id = user.id)
            usuario.save()

    return render(request,'registro.html',{"respuesta":respuesta})

def gmail(request):
    return render(request, 'gmail.html')

#def home(request):
#   return render(request, 'home.html')