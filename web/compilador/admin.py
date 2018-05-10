# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
	list_display=('id', 'nombre','apellido','contrasena','edad','ciudad','pais','lenguajePreferencia',)

