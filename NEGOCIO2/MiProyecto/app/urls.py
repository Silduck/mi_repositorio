from django.urls import path

from app import views

urlpatterns = [
    path('', views.mostrar_index, name='Inicio'),
    path('mostrar_clientes/', views.mostrar_clientes, name='Cliente'),
    path('personalLocal/', views.mostrar_personalLocal, name='Personal'),
    path('proveedores/', views.mostrar_proveedores, name='Proveedores'),	
    path('sucursales/', views.mostrar_sucursales, name='Sucursales'),
    path('productos/', views.mostrar_productos, name='Productos'),
    path('registrar_cliente/', views.registrar_cliente, name='Registrar Cliente'),
    path('buscar_articulo/', views.buscar_articulo, name='Buscar Articulo'),
    path('eliminar_cliente/<cliente_id>', views.eliminar_cliente, name= 'eliminar cliente'),
    path('cliente_confirm_delete/<pk>', views.ClientesDeleteView.as_view(), name= 'Delete'),
    path('actualizar_cliente/<cliente_id>',views.actualizar_cliente, name= 'actualizar cliente'),
    path('productos_list/', views.productosList.as_view(), name= 'List'),
    path('productos_detail/<pk>', views.productosDetailView.as_view(), name= 'Detail'),
    path('productos_confirm_delete/<pk>', views.productosDeleteView.as_view(), name= 'Delete'),
    path('productos_edit/<pk>', views.productosUpdateView.as_view(), name= 'Update'),
    path('productos_form/', views.productosCreateView.as_view(), name= 'Create'),
    path('buscar_tipo/', views.buscar_tipo, name= 'Buscar Tipo'),
    path('login/', views.login_request, name= 'Login'),
    path('register/', views.register, name = 'Register'),
    path('logout/', views.logout, name = 'Logout'),
    path('contacto/',views.contactenos, name= 'contactenos'),
    path('quienes_somos/',views.about, name= 'Quienes Somos'),
    ]
