from pyexpat import model
from django.db import models

# Create your models here.

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)


    def __str__(self):
            return  self.nombre 
    

class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
            return self.nombre 
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, max_length=100, on_delete=models.CASCADE)
    descripcion = models.TextField()
    esp_tecnica = models.TextField()
    imagen = models.ImageField(upload_to='productos/imagenes')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='productos/documentos')  # Campo para almacenar el archivo PDF

    
    def __str__(self):
            return str(self.tipo) + " " + self.nombre + " " + str(self.marca)
    

