# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

    #Alterando el formato de fecha
class ConvertingDateTimeField(models.DateTimeField):

    def get_prep_value(self, value):
        return str(datetime.strptime(value, FORMAT_STRING))

    # Create your models here.
class Usuarios(models.Model):
    ID_Usuario   = models.AutoField(primary_key=True)
    Tipo_Usuario = models.CharField(max_length=15)


    def __str__(self):
        return str(self.Tipo_Usuario)

class Clientes(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    Nombre     = models.CharField(max_length=50)
    Apellido   = models.CharField(max_length=50)
    Direccion  = models.CharField(max_length=50)
    Correo     = models.EmailField(max_length=50)
    #Usuario    = models.ForeignKey(Usuarios,on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.Nombre)

class Metodo_Pago(models.Model):
    ID_Metodo = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

class Pedidos(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL)
    ID_Pedido    = models.AutoField(primary_key=True)
    Cliente      = models.ForeignKey(Clientes,on_delete=models.CASCADE,)
    Fecha_Inicio = models.DateField()
    Fecha_Final  = models.DateField()
    Metodo_Pago  = models.ForeignKey(Metodo_Pago,on_delete=models.CASCADE)
    # Orden        = models.ManyToManyField(Productos,on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.ID_Pedido)

class Productos(models.Model):
    #user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    ID_Producto = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)
    Precio      = models.FloatField()
    imagen      = models.ImageField(upload_to='tamales/')

    def __str__(self):
        return str(self.Nombre)

class Pedido_Productos(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    ID          = models.AutoField(primary_key=True)
    Pedido      = models.ForeignKey(Pedidos,on_delete=models.CASCADE,)
    Producto    = models.ForeignKey(Productos,on_delete=models.CASCADE,)
    Cantidad    = models.PositiveSmallIntegerField()
    Total_Pagar = models.FloatField()

    def __str__(self):
        return str(self.Pedido)
