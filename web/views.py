from django.shortcuts import render
from front.models import Publicacion, Requisito, Beneficio
from babel.numbers import format_currency
from django import template
from .templatetags.local_currency import local_currency

# Create your views here.

def paginaweb(request):
    publicaciones = Publicacion.objects.filter(estado='activo').order_by('-fecha_creacion')    
    requisitos = Requisito.objects.all()
    print(requisitos.values())    
    
    
    return render(request, 'index.html', {'publicacion': publicaciones})
    

