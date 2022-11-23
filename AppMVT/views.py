from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.
def familia(request):
    persona1 = Familia(nombre="Pedro", edad=25, fecha="1997-03-27")
    persona2 = Familia(nombre="Ivana", edad=47, fecha="1975-03-13")
    persona3 = Familia(nombre="Dario", edad=49, fecha="1973-03-26")
    
    persona1.save()
    persona2.save()
    persona3.save()

    dic = {
        "nombre_persona1": persona1.nombre, "edad_persona1": persona1.edad, "fecha_persona1": persona1.fecha,
        "nombre_persona2": persona2.nombre, "edad_persona2": persona2.edad, "fecha_persona2": persona2.fecha,
        "nombre_persona3": persona3.nombre, "edad_persona3": persona3.edad, "fecha_persona3": persona3.fecha,
    }

    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(dic)

    return HttpResponse(documento)