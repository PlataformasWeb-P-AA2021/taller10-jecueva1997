from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

# Create your views here.

def index(request):
    """
        Listar los registros del modelo Estudiante, 
        obtenidos de la base de datos.
    """
    
    parroquias = Parroquia.objects.all()
    
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)

def listadoParroquias(request):
    """
    Listar los registros del modelo Parroquia, 
    obtenidos de la base de datos.
    """
    parroquias = Parroquia.objects.all()
    
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'listadoParroquias.html', informacion_template)

def listadoBarrios(request):
    """
    Listar los registros del modelo Barrios, 
    obtenidos de la base de datos.
    """
    barrios = Barrio.objects.all()

    informacion_template = {'barrios': barrios, 'numero_barrios': len(barrios)}
    return render(request, 'listadoBarrios.html', informacion_template)

def crear_parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario) 

def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 

def crear_barrio_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaBarrioForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaBarrioForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearParroquiaBarrio.html', diccionario) 


def editar_barrio(request, id):
    """
    """
    telefono = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=telefono)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=telefono)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario) 
