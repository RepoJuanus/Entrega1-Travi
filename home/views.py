from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from django.shortcuts import render, redirect
from home.forms import HumanoFormulario, BusquedaHumano

from home.models import Familiar

def hola(request):
    return HttpResponse('<h1>Bienvenidos a la clase !!!</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'<h3>La fecha y hora es: {fecha_actual}</h3>')  

def calcular_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años es {fecha}')

def mi_template(request):
    cargar_archivo = open(r'/Users/Ing.Travi/Documents/CodigoCODERHOUSE/Phyton/clases/Django/templates/template.html','r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context() 
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)

def mi_template_nombre(request, nombre):
       
    return render(request, 'home/template2.html', {"persona" : nombre} )

def prueba_template(request):
    
    mi_contexto = {"rango" : list(range (1,11)),
                   "valor_random" : random.randrange(1,11)}
         
    return render(request, 'home/prueba_template.html', mi_contexto )

def crear_familiares(request):
    
    familiar1 = Familiar(nombre = 'Juan', apellido = 'Gomez', edad = 50, fecha_nacimiento = datetime.now()-timedelta(50*365))
    familiar2 = Familiar(nombre = 'Carlos', apellido = 'Gomez', edad = 18, fecha_nacimiento = datetime.now()-timedelta(18*365))
    familiar3 = Familiar(nombre = 'Norma', apellido = 'Lopez', edad = 53, fecha_nacimiento = datetime.now()-timedelta(53*365))
    familiar1.save()     #guarda el objeto creado para que no desaparezca con el return
    familiar2.save()
    familiar3.save()
      
    mi_contexto = {"persona1" : familiar1,
                   "persona2" : familiar2,
                   "persona3" : familiar3}
    
    return render(request, 'home/crear_familiares.html', mi_contexto )

def crear_familiar(request):
    
    if request.method == 'POST':    # la primera vez que se accede a una vista, se hace por POST
        # print(request.method)
        # print('POST')
        # print(request.POST)
        # nombre = request.POST.get('nombre')
        # # apellido = request.POST.get('apellido')
        # apellido = request.POST['apellido']
        
        # persona = Familiar(nombre = nombre, apellido = apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
        # persona.save()
        # return redirect('ver_familia') # va a la URL
        
        formulario = HumanoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_nacimiento=data.get('fecha_nacimiento', datetime.now())
            persona = Familiar(nombre = nombre, apellido = apellido, edad=edad, fecha_nacimiento=fecha_nacimiento)
            persona.save()
            return redirect('ver_familia') # va a la URL
        
    formulario = HumanoFormulario()
    return render(request, 'home/crear_familiar.html', {'formulario': formulario} )
    
    # return render(request, 'home/crear_familiar.html', {} )


def ver_familiares(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre: 
        familiares = Familiar.objects.filter(nombre__icontains = nombre) #busca lo que contenga nombre
    else:
        familiares = Familiar.objects.all()
    
    formulario = BusquedaHumano()
    
    mi_contexto = {"familiares" : familiares, 'formulario': formulario}
    
    return render(request, 'home/ver_familiares.html', mi_contexto )

def index(request):
    return render(request, 'home/index.html')