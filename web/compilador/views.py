# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from  django.shortcuts import render


# Create your views here.

def login(request):
	#ordenar por id
	template=loader.get_template('index.html')
	
	return HttpResponse(template.render())

