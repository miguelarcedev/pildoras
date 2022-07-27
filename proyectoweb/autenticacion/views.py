from django.shortcuts import render

# Create your views here.

def atutenticacion(request):
    return render(request, "registro/registro.html")


