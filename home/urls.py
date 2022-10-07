from django.urls import path

from home import views
# se puede hacer asi tambien porque esta agregado el home el los paths

# from .views import hola, fecha 
# from . import views

urlpatterns = [
    path('', views.index),
    path('hola/', views.hola),
    path('fecha/', views.fecha),
    path('fecha-nacimiento/<int:edad>', views.calcular_nacimiento),
    path('fecha-nacimiento/', views.calcular_nacimiento),
    path('mi-template/<str:nombre>', views.mi_template_nombre),
    path('mi-template/', views.mi_template),
    path('prueba_template', views.prueba_template),
    path('ver-familiares/', views.ver_familiares),
    # path('crear-familiar/<str:nombre>/<str:apellido>/', views.crear_familiar),
    path('crear-familiares/', views.crear_familiares),
]
