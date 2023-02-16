from django.shortcuts import render
from .models import Project

def home(request):
    #Traemos todos los objetos almacenados en la bd
    projects=Project.objects.all()
    #Enviamos en un diccionario
    return render(request,'home.html',{'projects':projects})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def biography(request):
    return render(request,'biography.html')