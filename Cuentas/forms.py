from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User

class FormularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {campo:" " for campo in fields}



class MiFormularioEditar(UserChangeForm):
    first_name = forms.CharField(max_length=50,label="Nombre")
    last_name = forms.CharField(max_length=50,label="Apellido")
    password = None
    email = forms.EmailField(label="Modificar Mail")
    mipagina = forms.URLField(required=False) 
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email","first_name","last_name","mipagina","avatar"] 


class MiFormularioPassword(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Anterior", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Contraseña Nueva", widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput())

