from django.urls import path
from . import views
from .views import cliente_detail, crear_solicitud_prestamo, lista_solicitudes_prestamo_cliente

urlpatterns = [
    path('solicitar-prestamo/', views.solicitud_prestamo, name='solicitud_prestamo'),
    path('solicitud_exitosa/', views.solicitud_prestamo, name='solicitud_exitosa'),
    path('cliente-detail/<int:cliente_id>/', cliente_detail, name='cliente_detail'),
    path('crear-solicitud-prestamo/', crear_solicitud_prestamo, name='crear_solicitud_prestamo'),
    path('lista-solicitudes-prestamo-cliente/<int:cliente_id>/', lista_solicitudes_prestamo_cliente, name='lista_solicitudes_prestamo_cliente'),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Otras rutas de tu aplicación
#     path('', views.mi_vista_personalizada, name='ruta_personalizada'),
# ]
# En tu archivo urls.py


