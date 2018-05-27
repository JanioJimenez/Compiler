# -*- encoding:utf-8 -*-
from django import forms

from apps.usuario.models import Usuario

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        ]
        labels = {
        'username': 'Nombre de usuario',
        'first_name': 'Nombre',
        'last_name': 'Apellidos',
        'email': 'Correo',
        'password': 'Clave',
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
        'edad',
        'ciudad',
        'pais',
        'lenguaje',
        'usuario',
        ]
        labels = {
        'edad': 'Edad',
        'ciudad': 'Ciudad de origen',
        'pais': 'Pais de origen',
        'lenguaje': 'Lenguaje de preferencia',
        'usuario' : 'Id usuario',
        }