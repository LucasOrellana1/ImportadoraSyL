from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Producto

# Create your views here.


#Vistas:
def index(request):
    productos = Producto.objects.all()  # Recupera todos los productos

    return render(request, 'index.html', {'productos': productos})

def productos(request):
    return render(request, 'productos.html')

def about(request):
    return render(request, 'about.html')

def producto(request, id_producto):
    producto = get_object_or_404(Producto, pk=id_producto)
    return render(request, 'detalle_producto.html', {'producto': producto})



#BD:

