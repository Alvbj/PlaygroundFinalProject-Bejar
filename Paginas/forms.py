from django import forms

class ConsultaInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)

class CrearInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)
    tipo_instrumento = forms.CharField(max_length=50)
    precio_instrumento = forms.FloatField()
    descripcion_instrumento = forms.CharField(widget=forms.Textarea)
    fecha_incorporacion = forms.DateField()


class EditarInstrumento(forms.Form):
    nombre_instrumento = forms.CharField(max_length=50)
    tipo_instrumento = forms.CharField(max_length=50)
    precio_instrumento = forms.FloatField()


