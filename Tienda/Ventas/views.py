from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required    
# Create your views here.

class VentasView(TemplateView):
    template_name ="ventas.html"

def about(request):
    return HttpResponse("Hola soy la pagina de Acerca de")

@login_required
def bienvenida(request):
    if request.method == 'POST':
        return HttpResponse("Hola soy la pagina de bienvenida")
    else:
        return HttpResponse("Pagina no encontrada", status=404)
    
def buscar(request, nombre):
    return HttpResponse("Se va a buscar un producto con nombre " + nombre)

def listadoventas(request):
    return render(request, 'listadoventas.html')