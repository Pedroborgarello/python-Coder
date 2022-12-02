from django.shortcuts import render
from .models import Alumnos, Profesores, Materias
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def alumnos(request):
    persona1 = Alumnos(nombre="Pedro", fecha="1997-03-27", email="asdasd@asdas.com")
    persona2 = Alumnos(nombre="Ivana", fecha="1975-03-13", email="asdsasd@assdas.com")
    persona3 = Alumnos(nombre="Dario", fecha="1973-03-26", email="asdaasd@sasdas.com")
    
    persona1.save()
    persona2.save()
    persona3.save()

    """dic = {
        "nombre_persona1": persona1.nombre, "edad_persona1": persona1.edad, "fecha_persona1": persona1.fecha,
        "nombre_persona2": persona2.nombre, "edad_persona2": persona2.edad, "fecha_persona2": persona2.fecha,
        "nombre_persona3": persona3.nombre, "edad_persona3": persona3.edad, "fecha_persona3": persona3.fecha,
    }

    plantilla = loader.get_template('alumnos.html')
    documento = plantilla.render(dic)"""

    return render(request, "alumnos.html")

def profesores(request):
    if request.method== 'POST':
      nombre = request.POST["nombre"]
      profesion = request.POST["profesion"]
      email = request.POST["email"]

      profesor1 = Profesores(nombre=nombre, profesion=profesion, email=email)
      profesor1.save()
      return render(request, "inicio.html")
        
    return render(request, "profesores.html")

def materias(request):
    plantilla = loader.get_template('materias.html')
    documento = plantilla.render()

    return HttpResponse(documento)  

def inicio(request):
    
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()

    return render(request, "inicio.html")