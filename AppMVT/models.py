from django.db import models

# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido

class Materias(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField()