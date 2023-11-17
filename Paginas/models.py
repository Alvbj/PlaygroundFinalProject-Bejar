from django.db import models
from ckeditor.fields import RichTextField

class Instrumentos(models.Model):
    nombre_instrumento = models.CharField(max_length=50)
    tipo_instrumento = models.CharField(max_length=50)
    descripcion_instrumento = RichTextField(null=True)
    precio_instrumento = models.FloatField()
    fecha_incorporacion = models.DateField(null=True)
    imagen_instrumento = models.ImageField(upload_to="Instrumentos_images" ,null=True, blank=True)

    def __str__ (self):
        return f'{self.nombre_instrumento}'

