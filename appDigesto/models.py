from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Subcategoria(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Digesto(models.Model):
    numeroDigesto= models.CharField(max_length=15)
    estado = models.CharField(max_length=100)
    palabrasClave=models.TextField()
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='uploads/')
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_vigencia= models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.estado
