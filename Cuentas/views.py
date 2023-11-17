from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from Cuentas.forms import FormularioDeRegistro, MiFormularioEditar, MiFormularioPassword
from django.contrib.auth.views import PasswordChangeView
from Cuentas.models import InformacionAdicional

def login(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            
            usuario = authenticate(username=username, password=password)
            django_login(request, usuario)
            InformacionAdicional.objects.get_or_create(user=usuario)

            return redirect("inicio")
    else:
        formulario = AuthenticationForm()
    
    return render(request, r'Cuentas/login.html',{"formulario":formulario})


def registro(request):

    if request.method == "POST":
        formulario = FormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario = FormularioDeRegistro()
    
    return render(request, "Cuentas/registro.html",{"formulario":formulario})


def perfilusuario(request):
    usuario = request.user
    return render(request, "Cuentas/perfil.html",{"usuario":usuario})





def editarusuario(request):
   
    informacion_adicional = request.user.informacionadicional
   
    if request.method == "POST":
        formulario = MiFormularioEditar(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            informacion_adicional.mipagina = formulario.cleaned_data.get("mipagina")
            if formulario.cleaned_data.get("avatar"):
                informacion_adicional.avatar = formulario.cleaned_data.get("avatar")
            informacion_adicional.save()
            formulario.save()
            return redirect("inicio")
    else:
        formulario = MiFormularioEditar(initial={"mipagina":informacion_adicional.mipagina,"avatar":informacion_adicional.avatar},instance=request.user)
    
    return render(request, "Cuentas/editarusuario.html",{"formulario":formulario}) 



class CambioContraseña(PasswordChangeView):
    form_class = MiFormularioPassword
    template_name = "Cuentas/editarpass.html"
    success_url = reverse_lazy("editarusuario")