from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def autentificacion(request):
    return HttpResponse("<h1>Autentificación</h1")