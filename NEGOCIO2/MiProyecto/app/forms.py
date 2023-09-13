from django import forms 

class RegistrarClienteForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=40)
    telefono = forms.IntegerField()
    direccion = forms.CharField(min_length=3, max_length=30)

"""class BuscarProductosForm(forms.Form):
    articulo = forms.IntegerField()
    tipo = forms.CharField(min_length=2,max_length=20)
    estilo = forms.CharField(min_length= 3,max_length=20)
    color = forms.CharField(min_length=3,max_length=15)
    talle = forms.IntegerField ()"""


