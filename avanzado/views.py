from typing import List
from django.shortcuts import render, redirect
from avanzado.forms import MascotaFormulario
from avanzado.models import Mascota
from django.contrib.auth.mixins import LoginRequiredMixin #es para las cvb (mixin)
from django.contrib.auth.decorators import login_required #es para las vistas comunes (decoradores)
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def ver_mascotas(request):
    
    mascotas = Mascota.objects.all()

    return render(request, 'avanzado/ver_mascotas.html' , {'mascotas': mascotas})

@login_required
def crear_mascota(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota = Mascota( nombre = datos['nombre'] , 
                    tipo = datos['tipo'], 
                    edad = datos['edad'],
                    fecha_nacimiento = datos['fecha_nacimiento']
                    )
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'avanzado/crear_mascota.html' , {'formulario': formulario})
    
    formulario = MascotaFormulario()
    
    return render(request, 'avanzado/crear_mascota.html' , {'formulario': formulario})

def editar_mascota(request, id):
    
    mascota = Mascota.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
                        
            mascota.nombre = datos['nombre'] 
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            
            mascota.save()
            
            return redirect('ver_mascotas')

    formulario = MascotaFormulario(
        initial = {
            'nombre': mascota.nombre, 
            'tipo': mascota.tipo,
            'edad': mascota.edad, 
            'fecha_nacimiento': mascota.fecha_nacimiento
            }
        )

    return render(request, 'avanzado/editar_mascota.html' , {'formulario': formulario, 'mascota': mascota})

def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')

class ListaMascotas(ListView):
    model = Mascota
    template_name = 'avanzado/ver_mascotas_cvb.html'
    
class CrearMascota(CreateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'avanzado/crear_mascota_cvb.html'
    fields = ['nombre', 'tipo', 'edad','fecha_nacimiento']
    
class EditarMascota(LoginRequiredMixin, UpdateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'avanzado/editar_mascota_cvb.html'
    fields = ['nombre', 'tipo', 'edad','fecha_nacimiento']
    
class EliminarMascota(LoginRequiredMixin, DeleteView): #SIEMPRE el LoginRequiredMixin va como primera herencia
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'avanzado/eliminar_mascota_cvb.html'