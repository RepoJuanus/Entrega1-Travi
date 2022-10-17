from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('nosotros/', views.nosotros, name = 'nosotros'),
    path('ver-lista/', views.ver_lista, name = 'ver_lista'),
    path('crear-contacto/', views.crear_contacto, name = 'crear_contacto'),
]
