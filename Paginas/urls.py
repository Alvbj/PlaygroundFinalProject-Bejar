from django.urls import path
from Paginas.views import inicio, about, EnlaceVacio, consultainstrumento, crear_instrumento, editar_instrumento, eliminar_instrumento, DetalleInstrumentosView

urlpatterns = [
    path("",inicio,name="inicio"),
    path("enlacevacio/",EnlaceVacio.as_view(),name="enlacevacio"),
    path("about/",about,name="about"),
    path("instrumentos/",consultainstrumento,name="instrumentos"),
    path("instrumentos/crear/",crear_instrumento,name="crear_instrumentos"),
    path("instrumentos/<int:pk>/detalle/",DetalleInstrumentosView.as_view(),name="detalle_instrumentos"),
    path("instrumentos/<int:id_instrumento>/editar/",editar_instrumento,name="editar_instrumentos"),
    path("instrumentos/<int:id_instrumento>/eliminar/",eliminar_instrumento,name="eliminar_instrumentos"),
]
