from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

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