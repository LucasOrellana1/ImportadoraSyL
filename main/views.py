from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Marca, Producto, Tipo

# Create your views here.




#Vistas:
def index(request):
    productos = Producto.objects.all()  # Recupera todos los productos

    return render(request, 'index.html', {'productos': productos})

def productos(request):
    productos = Producto.objects.all()  # Recupera todos los productos
    filtros = ['Mezcladora' , 'Panel solar', 'Otro tipo', 'Escalera ascensor', 'Todos', "a"]
    filtros=  [ 'Todos','Escalera ascensor' , 'Panel solar' ]

    return render(request, 'productos.html', {'productos': productos, 'filtros': filtros})

def about(request):
    return render(request, 'about.html')


def contacto(request):
    return render(request, 'contacto.html')


def producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)

    relacionados = Producto.objects.all()

    return render(request, 'detalle_producto.html', {'producto': producto, 'relacionados' : relacionados})


#Servicios
def asbesto(request):
    return render(request, 'retiroAsbesto.html')

def construccion(request):
    return render(request, 'construccion.html')

def solar(request):
    return render(request, 'solar.html')

#BD:

