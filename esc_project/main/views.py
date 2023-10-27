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

    return render(request, 'productos.html', {'productos': productos})

def about(request):
    return render(request, 'about.html')


def contacto(request):
    return render(request, 'contacto.html')


def producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)

    relacionados = Producto.objects.all()

    return render(request, 'detalle_producto.html', {'producto': producto, 'relacionados' : relacionados})



#BD:

