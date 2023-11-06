from django.shortcuts import render

from app.models import Sucursales 

from app.models import Proveedores

from app.models import Personal

from app.models import Cliente

from app.models import Productos

from app.models import Contacto

from .forms import RegistrarClienteForm, UserRegisterForm, ContactoForm

from .forms import BuscarProductosForm

from django.views.generic import ListView 

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import BuscarTipoForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required 

from django.contrib.auth.views import LogoutView



def mostrar_sucursales (request):
    s1 = Sucursales(direccion='Hipolito Yrigoyen 1325', cuit=2569874521036, telefono=2204836985, instagram= '@calzadoslospatos', localidad='Merlo norte')
    s2 = Sucursales(direccion='av.LIbertador 196', cuit=305896321, telefono=2203058963, instagram= '@calzadoslospatos', localidad='Merlo centro') 
    s3 = Sucursales(direccion='Perón 1157', cuit=32213554654, telefono=2205454445, instagram= '@calzadoslospatos',localidad='Moron') 


    return render(request, 'app/sucursales.html',{'sucursales':[s1,s2,s3]})


def mostrar_proveedores (request):
    p1 = Proveedores(nombre='Santiago', apellido='Cardozo', telefono=4568389, direccion= 'Sullivan 489') 
    p2 = Proveedores(nombre='Juan', apellido='Perez', telefono=4987329, direccion= 'Avellaneda 4089')
    p3 = Proveedores(nombre='Gustavo', apellido='Capdevila', telefono=2204867899, direccion= 'Guardia vieja 1980')
    p4 = Proveedores(nombre='Horacio', apellido='Lopez', telefono=3956589, direccion= 'Uruguay 489')


    return render(request, 'app/proveedores.html',{'proveedores':[p1,p2,p3,p4]})

def mostrar_personalLocal (request):
    pl1 = Personal(nombre='Diego', apellido='Daro', edad=45, telefono= 1164592356) 
    pl2 = Personal(nombre='Ignacio', apellido='Perez', edad=54, telefono= 1166891235) 
    pl3 = Personal(nombre='Laura', apellido='Martiniano', edad=25, telefono= 1165517886) 
    pl4 = Personal(nombre='Ivanna', apellido='Gonzalez', edad=35, telefono= 1156324589) 


    return render(request, 'app/personalLocal.html',{'personalLocal':[pl1,pl2,pl3,pl4]})

#def mostrar_clientes(request):
    clienteslista =     Clientes.objects.all()

    return render(request, "app/mostrar_clientes.html", {"clientes": clienteslista})




def mostrar_clientes(request):

    clientes = Cliente.objects.all()

    context = {'clientes': clientes}

    return render(request, 'app/mostrar_clientes.html', context=context)

#def mostrar_clientes(request):
    c1 = Clientes(nombre='Diego', apellido='Daro',telefono= 220458631, direccion='av.libertador 1568') 
    c2 = Clientes(nombre='Ignacio', apellido='Perez', telefono= 1566891235, direccion='rivadavia 4586') 
    c3 = Clientes(nombre='Laura', apellido='Martiniano', telefono= 1565517886, direccion='brown 85421') 
    c4 = Clientes(nombre='Ivanna', apellido='Gonzalez',telefono= 1556324589, direccion='av peron 8452') 

    return render(request, 'app/mostrar_clientes.html',{'clientes':[c1,c2,c3,c4]})



def eliminar_cliente(request, cliente_id):

    cliente = Cliente.objects.get(id=cliente_id)

    cliente.delete() 

    clientes = Cliente.objects.all()

    context = {'clientes':clientes}

    return render(request, 'app/mostrar_clientes.html', context=context)

def actualizar_cliente(request, cliente_id):

    cliente = Cliente.objects.get(id=cliente_id)
    
    if request.method == 'POST':
        formulario = RegistrarClienteForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            cliente.nombre = formulario_limpio ['nombre']
            cliente.apellido = formulario_limpio ['apellido']
            cliente.telefono = formulario_limpio ['telefono']
            cliente.direccion = formulario_limpio ['direccion']

            cliente.save()

            return render(request, 'app/home.html')
        else:
            formulario = RegistrarClienteForm(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 
                                                    'telefono': cliente.telefono, 'direccion': cliente.direccion})
            
    return render(request, 'app/actualizar_cliente.html',{'formulario': RegistrarClienteForm, 'cliente': cliente})
                                        

            



def mostrar_productos (request):
    pd1 = Productos(articulo=1020, tipo='zapatilla',estilo= 'running', color='negro', precio=30299) 
    pd2 = Productos(articulo=1030, tipo='zapatilla',estilo= 'urbano', color='negro', precio=30349) 
    pd3 = Productos(articulo=1040, tipo='zapatilla',estilo= 'running', color='blanco', precio=35049) 
    pd4 = Productos(articulo=1021, tipo='zapatilla',estilo= 'urbano', color='violeta', precio=32399) 


    return render(request, 'app/productos.html',{'productos':[pd1,pd2,pd3,pd4]})
@login_required
def mostrar_index(request):



    return render(request, 'app/home.html')

def registrar_cliente(request):

    if request.method == 'POST':

        formulario = RegistrarClienteForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            cliente = Cliente(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], telefono=formulario_limpio['telefono'], direccion=formulario_limpio['direccion'])

            cliente.save()

            return render(request, 'app/home.html')
    else:
            formulario = RegistrarClienteForm()

    return render(request, 'app/registrar_cliente.html', {'formulario': RegistrarClienteForm})

def buscar_articulo(request):

    if request.GET.get('articulo', False):
        articulo = request.GET['articulo']
        producto = Productos.objects.filter(articulo__icontains=articulo)

        return render(request, 'app/buscar_productos.html', {'producto': producto})
    else:
        respuesta = 'No hay datos'
    return render(request, 'app/buscar_productos.html', {'respuesta': respuesta})

class productosList(LoginRequiredMixin, ListView):

    model= Productos
    template_name = 'app/productos_list.html'

class productosCreateView(CreateView):

    model = Productos
    success_url = '/productos_list'
    fields = ['articulo', 'tipo', 'estilo', 'color', 'precio']

class productosDetailView(LoginRequiredMixin, DetailView):

    model = Productos
    template_name = 'app/productos_detalle.html'

class productosDeleteView(LoginRequiredMixin, DeleteView):

    model = Productos
    success_url = '/productos_list'

class productosUpdateView(LoginRequiredMixin, UpdateView):

    model = Productos
    success_url = '/productos_list'
    fields = ['articulo', 'tipo', 'estilo', 'color', 'precio']


class ClientesDeleteView(DeleteView):

    model = Cliente
    success_url = '/clientes_list'

class AdminLogoutView(LogoutView):
    template_name = 'app/logout.html'


def buscar_tipo(request):
    if request.GET.get('tipo', False):
        tipo = request.GET['tipo']
        producto = Productos.objects.filter(tipo__icontains=tipo)

        return render(request, 'app/buscar_tipo.html', {'producto': producto})
    else:
        respuesta = 'No hay datos'
    return render(request, 'app/buscar_tipo.html', {'respuesta': respuesta})

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request,'app/home.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'app/home.html', {"mensaje":"Error,datos incorrectos"})
            
        else:
            return render(request,'app/home.html', {"mensaje":"Error,formulario erroneo"})
    form = AuthenticationForm()

    return render(request, 'app/login.html', {'form':form})

def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'app/home.html', {"mensaje":"usuario creado"})
        else:
                form = UserCreationForm()
        return render(request, 'app/registro.html', {"form":form})
    
def contactenos(request):

    if request.method == 'POST':

        formulario = ContactoForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            consulta = Contacto(nombre=formulario_limpio['nombre'], email=formulario_limpio['email'], telefono=formulario_limpio['telefono'], mensaje=formulario_limpio['mensaje'])

            consulta.save()

            return render(request, 'app/home.html')
    else:
            formulario = ContactoForm()

    return render(request, 'app/contactanos.html', {'formulario': ContactoForm})

def about(request):

    return render(request, 'app/nosotros.html')
    






