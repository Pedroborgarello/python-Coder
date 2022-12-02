from django.shortcuts import render
from .models import Alumnos, Profesores, Materias
from django.http import HttpResponse
from django.template import loader
from AppMVT.forms import ProfesoresForm, AlumnosForm, MateriasForm

# Create your views here.
def alumnos(request):
    if request.method== 'POST':
      form = AlumnosForm(request.POST)

      if form.is_valid():
        info = form.cleaned_data
      
        nombre = info["nombre"]
        fecha = info["fecha"]
        email = info["email"]

        alumno1 = Alumnos(nombre=nombre, fecha=fecha, email=email)
        alumno1.save()
        return render(request, "inicio.html")
    else:
        formulario = AlumnosForm()
        
    return render(request, "alumnos.html", {"form":formulario})
    

def profesores(request):
    if request.method== 'POST':
      form = ProfesoresForm(request.POST)

      if form.is_valid():
        info = form.cleaned_data
      
        nombre = info["nombre"]
        profesion = info["profesion"]
        email = info["email"]

        profesor1 = Profesores(nombre=nombre, profesion=profesion, email=email)
        profesor1.save()
        return render(request, "inicio.html")
    else:
        formulario = ProfesoresForm()
        
    return render(request, "profesores.html", {"form":formulario})

def materias(request):
    if request.method== 'POST':
      form = MateriasForm(request.POST)

      if form.is_valid():
        info = form.cleaned_data
      
        nombre = info["nombre"]
        nivel = info["nivel"]

        materia1 = Profesores(nombre=nombre, nivel=nivel)
        materia1.save()
        return render(request, "inicio.html")
    else:
        formulario = MateriasForm()
        
    return render(request, "materias.html", {"form":formulario})  

def inicio(request):
    
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()

    return render(request, "inicio.html")