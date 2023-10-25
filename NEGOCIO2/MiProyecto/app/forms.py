from django import forms 

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import User 

class RegistrarClienteForm(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=40)
    telefono = forms.IntegerField()
    direccion = forms.CharField(min_length=3, max_length=30)

class BuscarProductosForm(forms.Form):
    articulo = forms.IntegerField()
    tipo = forms.CharField(min_length=2,max_length=20)
    estilo = forms.CharField(min_length= 3,max_length=20)
    color = forms.CharField(min_length=3,max_length=15)
    precio = forms.IntegerField()

class BuscarTipoForm(forms.Form):
    articulo = forms.IntegerField()
    tipo = forms.CharField(min_length=3, max_length=15)
    estilo = forms.CharField(min_length=3, max_length=15)
    color = forms.CharField(min_length=2, max_length=15)
    precio = forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {k:"" for k in fields}


