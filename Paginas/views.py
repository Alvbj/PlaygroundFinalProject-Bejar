from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from Paginas.forms import ConsultaInstrumento, CrearInstrumento, EditarInstrumento
from Paginas.models import Instrumentos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView


def inicio (request):
    return render(request, r'Paginas\inicio.html')

def about(request):
    return render(request, r'Paginas\about.html')

class EnlaceVacio(TemplateView):
    template_name = "Paginas/enlacevacio.html"



def consultainstrumento (request):
    formulario = ConsultaInstrumento(request.GET)
    if formulario.is_valid():
        data = formulario.cleaned_data.get("nombre_instrumento")
        instrumento_buscado = Instrumentos.objects.filter(nombre_instrumento__icontains = data)
    else:
        instrumento_buscado = Instrumentos.objects.all()
    
    formulario = ConsultaInstrumento()
    return render(request, r'Paginas\instrumentos.html',{"formulario":formulario, "instrumento_buscado":instrumento_buscado})


@login_required
def crear_instrumento (request):

    if request.method == "POST":
        formulario = CrearInstrumento(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            instrumento = Instrumentos(nombre_instrumento=data.get("nombre_instrumento"),tipo_instrumento=data.get("tipo_instrumento"),precio_instrumento=data.get("precio_instrumento"),descripcion_instrumento=data.get("descripcion_instrumento"),fecha_incorporacion=data.get("fecha_incorporacion"),imagen_instrumento=data.get("imagen_instrumento"))
            instrumento.save()
            return redirect("instrumentos") 
        else:
            return render(request, r'Paginas\crearinstrumentos.html',{"formulario":formulario})        

    formulario = CrearInstrumento()
    return render(request, r'Paginas\crearinstrumentos.html',{"formulario":formulario})


@login_required
def editar_instrumento (request, id_instrumento):

    instrumento_a_editar = Instrumentos.objects.get(id=id_instrumento)
    
    if request.method == "POST":
        formulario = EditarInstrumento(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            instrumento_a_editar.nombre_instrumento = data["nombre_instrumento"]
            instrumento_a_editar.tipo_instrumento = data["tipo_instrumento"]
            instrumento_a_editar.precio_instrumento = data["precio_instrumento"]
            instrumento_a_editar.descripcion_instrumento = data["descripcion_instrumento"]
            instrumento_a_editar.fecha_incorporacion = data["fecha_incorporacion"]
            instrumento_a_editar.imagen_instrumento = data["imagen_instrumento"]
            instrumento_a_editar.save()
            return redirect("instrumentos")
        else:
            return render(request, r'Paginas/editarinstrumentos.html', {"formulario":formulario})


    formulario = EditarInstrumento(initial={"nombre_instrumento":instrumento_a_editar.nombre_instrumento, "tipo_instrumento":instrumento_a_editar.tipo_instrumento, "precio_instrumento":instrumento_a_editar.precio_instrumento})

    return render(request, r'Paginas/editarinstrumentos.html', {"formulario":formulario})

@login_required
def eliminar_instrumento (request, id_instrumento):

    instrumento_a_eliminar = Instrumentos.objects.get(id=id_instrumento)
    instrumento_a_eliminar.delete()

    return redirect("instrumentos")


class DetalleInstrumentosView(DetailView):
    model = Instrumentos
    template_name = "Paginas/detalleinstrumentos.html"
    context_object_name = "instrumento_detallado"

    def get_queryset(self):
        return Instrumentos.objects.filter(pk=self.kwargs["pk"])


