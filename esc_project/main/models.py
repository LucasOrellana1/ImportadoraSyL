from pyexpat import model
from django.db import models

# Create your models here.


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    esp_tecnica = models.TextField()
    imagen = models.ImageField(upload_to='productos/imagenes')

    def __str__(self):
            return self.nombre + " " + self.marca
