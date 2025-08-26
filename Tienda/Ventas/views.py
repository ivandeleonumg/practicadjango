from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class VentasView(TemplateView):
    template_name ="ventas.html"