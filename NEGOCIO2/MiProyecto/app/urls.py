from django.urls import path

from app import views

urlpatterns = [
    path('', views.mostrar_index, name='Inicio'),
    path('mostrar_clientes/', views.mostrar_index, name='Clientes'),
    path('personalLocal/', views.mostrar_personalLocal, name='PersonalLocal'),
    path('proveedores/', views.mostrar_proveedores, name='Proveedores'),	
    path('sucursales/', views.mostrar_sucursales, name='Sucursales'),
    path('productos/', views.mostrar_productos, name='Productos'),
    path('registrar_cliente/', views.registrar_cliente, name='Registrar Cliente'),
    path('buscar_articulo/', views.buscar_articulo, name='Buscar Articulo'),
    path('eliminar_cliente/<cliente_id>', views.eliminar_cliente, name= 'eliminar cliente')
]
