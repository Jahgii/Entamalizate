# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

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
    Usuario    = models.ForeignKey(Usuarios,on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.Nombre)

class Metodo_Pago(models.Model):
    ID_Metodo = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Nombre)

class Pedidos(models.Model):
    ID_Pedido    = models.AutoField(primary_key=True)
    Cliente      = models.ForeignKey(Clientes,on_delete=models.CASCADE,)
    Fecha_Inicio = models.DateTimeField()
    Fecha_Final  = models.DateTimeField()
    Metodo_Pago  = models.ForeignKey(Metodo_Pago,on_delete=models.CASCADE)
    # Orden        = models.ManyToManyField(Productos,on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.ID_Pedido)

class Productos(models.Model):
    ID_Producto = models.AutoField(primary_key=True)
    Nombre      = models.CharField(max_length=50)
    Precio      = models.FloatField()

    def __str__(self):
        return str(self.Nombre)

class Pedido_Productos(models.Model):
    ID          = models.AutoField(primary_key=True)
    Pedido      = models.ForeignKey(Pedidos,on_delete=models.CASCADE,)
    Producto    = models.ForeignKey(Productos,on_delete=models.CASCADE,)
    Cantidad    = models.PositiveSmallIntegerField()
    Total_Pagar = models.FloatField()

    def __str__(self):
        return str(self.Pedido)
