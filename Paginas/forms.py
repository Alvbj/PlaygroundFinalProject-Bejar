from django import forms
from ckeditor.fields import RichTextFormField

class CrearInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)
    tipo_instrumento = forms.CharField(max_length=50)
    precio_instrumento = forms.FloatField()
    descripcion_instrumento = RichTextFormField()
    fecha_incorporacion = forms.DateField()
    imagen_instrumento = forms.ImageField()


class EditarInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)
    tipo_instrumento = forms.CharField(max_length=50)
    precio_instrumento = forms.FloatField()
    descripcion_instrumento = RichTextFormField()
    fecha_incorporacion = forms.DateField()
    imagen_instrumento = forms.ImageField()

class ConsultaInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)