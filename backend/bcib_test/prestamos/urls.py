from django.urls import path
from . import views

urlpatterns = [
    path('solicitar-prestamo/', views.solicitud_prestamo, name='solicitud_prestamo'),
    path('solicitud_exitosa/', views.solicitud_prestamo, name='solicitud_exitosa'),

]
