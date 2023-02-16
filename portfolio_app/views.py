from django.shortcuts import render
from .models import Project

def home(request):
    #Traemos todos los objetos almacenados en la bd
    projects=Project.objects.all()
    #Enviamos en un diccionario
    return render(request,'home.html',{'projects':projects})
