from django.db import models

from django.db import models

class CatParaf(models.Model):
    id_cat_paraf = models.AutoField(primary_key=True, db_column='idCatParaf')
    nombre_tipo = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombre_tipo

class Parafernalia(models.Model):
    idparaf = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    id_cat_paraf = models.ForeignKey(CatParaf, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='items', null=True)

    def __str__(self):
        return self.nombre
