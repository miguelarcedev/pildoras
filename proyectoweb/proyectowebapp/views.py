from urllib import response
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, "proyectowebapp/home.html")

def tienda(request):
    return render(request, "proyectowebapp/tienda.html")

def contacto(request):
    return render(request, "proyectowebapp/contacto.html")