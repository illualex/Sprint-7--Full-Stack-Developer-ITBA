from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente


class TipoPrestamo(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class SolicitudPrestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # tipo_prestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)
    tipo_prestamo = models.ForeignKey(TipoPrestamo, db_column='loan_type', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobado = models.BooleanField(default=False)

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    user_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'prestamo'
