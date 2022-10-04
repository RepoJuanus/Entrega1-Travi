from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

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
   
    template = loader.get_template("template2.html")
    template_renderizado = template.render({"persona" : nombre})
    
    return HttpResponse(template_renderizado)

def prueba_template(request):
    
    mi_contexto = {"rango" : list(range (1,11)),
                   "valor_random" : random.randrange(1,11)}
        
    template = loader.get_template("prueba_template.html")
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)

# def crear_familiar(request, nombre, apellido):
    
#     familiar = Familiar(nombre=nombre, apellido=apellido, edad= random.randrange(1,99), fecha_nacimiento=datetime.now())
#     familiar.save()     #guarda el objeto creado para que no desaparezca con el return
    
#     mi_contexto = {"persona" : familiar}
#     template = loader.get_template("crear_familiar.html")
#     template_renderizado = template.render(mi_contexto)     
        
#     return HttpResponse(template_renderizado)

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
    
    template = loader.get_template("crear_familiares.html")
    template_renderizado = template.render(mi_contexto)     
        
    return HttpResponse(template_renderizado)


def ver_familiares(request):
    
    familiares = Familiar.objects.all()
    mi_contexto = {"familiares" : familiares}
    template = loader.get_template("ver_familiares.html")
    template_renderizado = template.render(mi_contexto) 
        
    return HttpResponse(template_renderizado)