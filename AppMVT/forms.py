from django import forms

class ProfesoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=50)
    email = forms.EmailField()

class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    fecha = forms.DateField()
    email = forms.EmailField()

class MateriasForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    nivel = forms.IntegerField()