from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto= models.CharField(max_length= 40)
    precio= models.IntegerField()
    stock= models.BooleanField()

class Vendedor(models.Model):
    nombre_apellido= models.CharField(max_length= 40)
    mail= models.EmailField()
    codigo_interno= models.IntegerField()

class Categoria(models.Model):
    tipo= models.CharField(max_length= 40)
    estado= models.CharField(max_length= 40)
    tamanio= models.DecimalField(max_digits=6,decimal_places= 3)