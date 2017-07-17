from django.shortcuts import render
from django.views.generic import TemplateView

class index(TemplateView):

    template_name = 'hola.html'

class prueba(TemplateView):
    template_name = 'prueba.html'

class inicio(TemplateView):
    template_name = 'index.html'