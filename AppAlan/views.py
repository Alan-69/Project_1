from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppAlan/index.html")

def cursos(request):
    return render(request, "AppAlan/cursos.html")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")
