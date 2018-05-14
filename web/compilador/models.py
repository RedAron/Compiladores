# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# nombres, los apellidos, edad, ciudad de origen,país y lenguaje de preferencia
# Create your models here.
class Usuario(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=35)
    contrasena=models.CharField(max_length=30)
    apellido=models.CharField(max_length=40,default=" ")
    edad=models.CharField(max_length=3,default=" ")
    ciudad=models.CharField(max_length=40,default=" ")
    pais=models.CharField(max_length=40,default="  ")
    lenguajePreferencia=models.CharField(max_length=15,default=" ")

    
    
    def __str__(self):
        return self.nombre

class Meta:
    ordering=('id',)
