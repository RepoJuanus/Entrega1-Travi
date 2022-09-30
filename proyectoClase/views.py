from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

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