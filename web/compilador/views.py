# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from  django.shortcuts import render
from .forms import UsuariosForm


# Create your views here.

def login(request):
	#ordenar por id
	template=loader.get_template('index.html')
	context={
	}
	
	return HttpResponse(template.render(context,request))

def new_Usuario(request):
	if request.method=='POST':
		form=UsuariosForm(request.POST,request.FILES)
		if form.is_valid():
			Usuario=form.save()
			Usuario.save()
			return HttpResponseRedirect('/')
	else:
		form=UsuariosForm

	template=loader.get_template('registro.html')
	title="nuevo usuario"
	context={
		'form': form,
		'title':title
         }
	return HttpResponse(template.render(context,request))