from django import forms

class CrearContacto(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=30)
    email = forms.EmailField(min_length=5, max_length=60, required=False) #, help_text='example@example.com')  # no es requerido obligatorio
    
class BuscarContacto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    apellido = forms.CharField(max_length=30, required=False)