from django.urls import path
from . import views

urlpatterns = [
    path('solicitar-prestamo/', views.solicitud_prestamo, name='solicitud_prestamo'),
    path('solicitud_exitosa/', views.solicitud_prestamo, name='solicitud_exitosa'),

]
# from django.urls import path
# from . import views

# urlpatterns = [
#     # Otras rutas de tu aplicación
#     path('', views.mi_vista_personalizada, name='ruta_personalizada'),
# ]