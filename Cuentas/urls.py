from django.urls import path
from Cuentas.views import login, registro, editarusuario, perfilusuario, CambioContraseña
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/",login,name="login"),
    path("registro/",registro,name="registro"),
    path("perfil/",perfilusuario,name="perfil"),
    path("perfil/editarusuario/",editarusuario,name="editarusuario"),
    path("perfil/editarusuario/editarpass/",CambioContraseña.as_view(),name="editarpass"),
    path("logout/",LogoutView.as_view(template_name="Cuentas/logout.html"),name="logout"),
]