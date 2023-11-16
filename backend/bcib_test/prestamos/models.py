from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    USUARIO_CHOICES = (
        ('BLACK', 'BLACK'),
        ('GOLD', 'GOLD'),
        ('CLASSIC', 'CLASSIC'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cliente = models.CharField(max_length=20, choices=USUARIO_CHOICES)

class TipoPrestamo(models.Model):
    tipo = models.CharField(max_length=50)
    monto_maximo = models.DecimalField(max_digits=10, decimal_places=2)

class SolicitudPrestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobado = models.BooleanField(default=False)
