from django.urls import path
from AppMVT.views import *

urlpatterns = [
    path("alumnos/", alumnos, name="alumnos"),
    path("profesores/", profesores, name="profesores"),
    path("materias/", materias, name="materias"),
    path("", inicio, name="inicio"),
]