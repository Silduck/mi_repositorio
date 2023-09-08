from django.db import models

# Create your models here.

class proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)

class personalLocal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    telefono = models.DateField()

class clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Telefono: {self.telefono}, Direccion: {self.direccion}'


#class localidad(models.Model):
 #   nombre = models.CharField(max_length=40)


class sucursales(models.Model):
    direccion = models.CharField(max_length=40)
    cuit = models.IntegerField()
    telefono = models.IntegerField()
    instagram= models.CharField(max_length=40)
    localidad = models.CharField(max_length=50)

    def __str__(self):
        return f'Direccion: {self.direccion}, Cuit: {self.cuit}, Telefono: {self.telefono}, Instagram: {self.instagram}, Localidad: {self.localidad}'

class productos(models.Model):
    articulo = models.IntegerField()
    tipo = models.CharField(max_length=20)
    estilo = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    talle = models.IntegerField ()

    def __str__(self):
        return f'Articulo: {self.articulo}, Tipo: {self.tipo}, Estilo: {self.estilo}, Color: {self.color}, Talle: {self.talle}'

