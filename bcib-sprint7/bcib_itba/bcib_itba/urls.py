from django.contrib import admin
from django.urls import path, include
from prestamos.views import prestamos_view
from home.views import home_view
from login.views import login_view
from perfil.views import perfil_view
from tarjetas.views import tarjetas_view
from personal_data.views import data_view
from register.views import register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prestamos/', prestamos_view),
    path("", home_view),
    path("login/", login_view),
    path("perfil/", perfil_view),
    path("tarjetas/", tarjetas_view),
    path("personal_data/", data_view),
    path("registro/", register_view),
    path('accounts/', include('django.contrib.auth.urls')),
]
