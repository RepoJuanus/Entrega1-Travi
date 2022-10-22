
from re import template
from django.shortcuts import render, redirect
from home.forms import CrearContacto, BuscarContacto

from home.models import Contacto

def crear_contacto(request):
    if request.method == 'POST':    # la primera vez que se accede a una vista, se hace por POST
        formulario = CrearContacto(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            telefono = data['telefono']
            
            contacto = Contacto(nombre = nombre, apellido = apellido, telefono=telefono)
            contacto.save()
            return redirect('ver_lista') # va a la URL
    formulario = CrearContacto()
    return render(request, 'home/crear_contacto.html', {'formulario': formulario} )
    
def ver_lista(request):
    nombre = request.GET.get('nombre', None)
    apellido = request.GET.get('apellido', None)
    if nombre and not apellido:
        contactos = Contacto.objects.filter(nombre__icontains = nombre) #busca lo que contenga nombre
    elif apellido and not nombre:
        contactos = Contacto.objects.filter(apellido__icontains = apellido) #busca lo que contenga apellido
    elif nombre and apellido:
        contactos = Contacto.objects.filter(apellido__icontains = apellido, nombre__icontains = nombre) #busca lo que contenga apellido        
    else: 
        contactos = Contacto.objects.all()
               
    formulario = BuscarContacto()
    
    mi_contexto = {"contactos" : contactos, 'formulario': formulario}
    return render(request, 'home/ver_lista.html', mi_contexto )

def nosotros(request):
    return render(request, 'home/nosotros.html')
    # return redirect('nosotros')
    
def index(request):
    return render(request, 'home/index.html')