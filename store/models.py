from django.db import models

# Create your models here.


class Parafernalia(models.Model):
    idparaf = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='items')

    def __str__(self):
        return self.nombre
