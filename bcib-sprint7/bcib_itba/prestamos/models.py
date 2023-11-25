# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'
