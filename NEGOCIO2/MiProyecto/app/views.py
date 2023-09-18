from django.shortcuts import render

from app.models import sucursales 

from app.models import proveedores

from app.models import personalLocal

from app.models import clientes

from app.models import productos

from .forms import RegistrarClienteForm

from .forms import BuscarProductosForm

# Create your views here.


def mostrar_sucursales (request):
    s1 = sucursales(direccion='Hipolito Yrigoyen 1325', cuit=2569874521036, telefono=2204836985, instagram= '@mundoshoes', localidad='Merlo')
    s2 = sucursales(direccion='av.LIbertador 196', cuit=305896321, telefono=305896321, instagram= '@mundoshoes', localidad='Merlo') 
    s3 = sucursales(direccion='Perón 1157', cuit=32213554654, telefono=54544456, instagram= '@mundoshoes',localidad='Moron') 


    return render(request, 'app/sucursales.html',{'sucursales':[s1,s2,s3]})


def mostrar_proveedores (request):
    p1 = proveedores(nombre='Santiago', apellido='Cardozo', telefono=45683892, direccion= 'cetra 489') 
    p2 = proveedores(nombre='juan', apellido='Perez', telefono=49873292, direccion= 'avellaneda 4089')
    p3 = proveedores(nombre='Gustavo', apellido='Capdevila', telefono=48678992, direccion= 'kiernan 5989')
    p4 = proveedores(nombre='Horacio', apellido='Lopez', telefono=39565892, direccion= 'Uruguay 489')


    return render(request, 'app/proveedores.html',{'proveedores':[p1,p2,p3,p4]})

def mostrar_personalLocal (request):
    pl1 = personalLocal(nombre='Diego', apellido='Daro', edad=45, telefono= 1564592356) 
    pl2 = personalLocal(nombre='Ignacio', apellido='Perez', edad=54, telefono= 1566891235) 
    pl3 = personalLocal(nombre='Laura', apellido='Martiniano', edad=25, telefono= 1565517886) 
    pl4 = personalLocal(nombre='Ivanna', apellido='Gonzalez', edad=35, telefono= 1556324589) 


    return render(request, 'app/personalLocal.html',{'personalLocal':[pl1,pl2,pl3,pl4]})


def mostrar_clientes (request):
    c1 = clientes(nombre='Diego', apellido='Daro',telefono= 1564592356, direccion='mariano acosta 111') 
    c2 = clientes(nombre='Ignacio', apellido='Perez', telefono= 1566891235, direccion='rivadavia 4586') 
    c3 = clientes(nombre='Laura', apellido='Martiniano', telefono= 1565517886, direccion='brown 85421') 
    c4 = clientes(nombre='Ivanna', apellido='Gonzalez',telefono= 1556324589, direccion='av peron 8452') 


    return render(request, 'app/clientes.html',{'clientes':[c1,c2,c3,c4]})


def mostrar_productos (request):
    pd1 = productos(articulo=1020, tipo='zapatilla',estilo= 'running', color='negro', talle=35) 
    pd2 = productos(articulo=1030, tipo='zapatilla',estilo= 'urbano', color='negro', talle=35) 
    pd3 = productos(articulo=1040, tipo='zapatilla',estilo= 'running', color='blanco', talle=35) 
    pd4 = productos(articulo=1021, tipo='zapatilla',estilo= 'urbano', color='violeta', talle=35) 


    return render(request, 'app/productos.html',{'productos':[pd1,pd2,pd3,pd4]})

def mostrar_index(request):



    return render(request, 'app/home.html')

def registrar_cliente(request):

    if request.method == 'POST':

        formulario = RegistrarClienteForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            cliente = clientes(nombre=formulario_limpio['nombre'], apellido=formulario_limpio['apellido'], telefono=formulario_limpio['telefono'], direccion=formulario_limpio['direccion'])

            cliente.save()

            return render(request, 'app/home.html')
    else:
            formulario = RegistrarClienteForm()

    return render(request, 'app/registrar_cliente.html', {'formulario': RegistrarClienteForm})

def buscar_articulo(request):

    if request.GET.get('articulo', False):
        articulo = request.GET['articulo']
        producto = productos.objects.filter(articulo__icontains=articulo)

        return render(request, 'app/buscar_productos.html', {'producto': producto})
    else:
        respuesta = 'No hay datos'
    return render(request, 'app/buscar_productos.html', {'respuesta': respuesta})



