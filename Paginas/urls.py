from django.urls import path
from Paginas.views import inicio

urlpatterns = [
    path("inicio/",inicio,name="inicio")
]
