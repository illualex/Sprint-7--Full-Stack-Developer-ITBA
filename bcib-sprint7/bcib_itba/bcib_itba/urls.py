"""
URL configuration for bcib_itba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
from logout.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prestamos/', prestamos_view),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name='logout'),
    path("perfil/", perfil_view),
    path("tarjetas/", tarjetas_view),
    path("personal_data/", data_view),
    path("registro/", register_view),
    path("", home_view),
]
