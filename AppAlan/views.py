from django.shortcuts import render
from django.http import HttpResponse
from AppAlan.models import *

def inicio(request):
    return render(request, "AppAlan/index.html")

def cursos(request):
    return render(request, "AppAlan/cursos.html")

def profesores(request):
    return render(request, "AppAlan/profesores.html")

def estudiantes(request):
    return render(request, "AppAlan/estudiantes.html")

def entregables(request):
    return render(request, "AppAlan/entregables.html")



def curso_formulario(request):
    if request.method ==  'POST':
        
        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()
        
        return render(request, "AppAlan/index.html")
    return render(request,"AppAlan/curso_formulario.html")