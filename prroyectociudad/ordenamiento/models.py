from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Parroquia(models.Model):
    opciones_tipo = (
        ('urbana', 'Parroquia Urbana'),
        ('rural', 'Parroquia Rural'),
    )
    nombre = models.CharField(max_length=30, unique=True)
    tipo_parroquia = models.CharField(max_length=30, \
        choices=opciones_tipo)

    def __str__(self):
        return "%s " % (self.nombre)

class Barrio(models.Model):
    numero_parque = (
        (1, "1 Parque"),
        (2, "2 Parques"),
        (3, "3 Parques"),
        (4, "4 Parques"),
        (5, "5 Parques"),
        (6, "6 Parques"),
    )
    nombre = models.CharField(max_length=100, unique=True)
    numero_vivienda = models.IntegerField("numero de viviendas")
    parque = models.IntegerField(choices=numero_parque) 
    numero_edificio = IntegerField("numero de edificios")
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, \
            related_name="barrio")

    def __str__(self):
        return "%s - %d - %d - %d " % (self.nombre, 
                self.numero_vivienda,
                self.parque,
                self.numero_edificio)
