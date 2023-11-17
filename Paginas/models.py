from django.db import models

class Instrumentos(models.Model):
    nombre_instrumento = models.CharField(max_length=50)
    tipo_instrumento = models.CharField(max_length=50)
    descripcion_instrumento = models.TextField(null=True)
    precio_instrumento = models.FloatField()
    fecha_incorporacion = models.DateField(null=True)

    def __str__ (self):
        return f'{self.nombre_instrumento}'


class Amplificadores(models.Model):
    nombre_artefacto = models.CharField(max_length=50)
    tipo_artefacto = models.CharField(max_length=50)
    precio_amplificador = models.FloatField()

    def __str__ (self):
        return f'{self.nombre_artefacto}'
