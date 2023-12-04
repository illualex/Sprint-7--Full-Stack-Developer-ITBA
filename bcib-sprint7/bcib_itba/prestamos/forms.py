from django import forms
from .models import SolicitudPrestamo, TipoPrestamo, Cliente

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = SolicitudPrestamo
        fields = ['monto_solicitado', 'tipo_prestamo', 'fecha_inicio']

    def clean(self):
        cleaned_data = super().clean()
        cliente = Cliente.objects.get(user=self.instance.cliente.user)
        monto_solicitado = cleaned_data.get('monto_solicitado')
        tipo_prestamo = cleaned_data.get('tipo_prestamo')

        # Establecer los límites de préstamo según el tipo de cliente
        if cliente.tipo_cliente == 'BLACK':
            max_monto = 500000
        elif cliente.tipo_cliente == 'GOLD':
            max_monto = 300000
        else:
            max_monto = 100000

        # Validar si el monto solicitado supera el límite para este tipo de préstamo
        if monto_solicitado > max_monto:
            raise forms.ValidationError("El monto solicitado supera el límite para este tipo de cliente")

        return cleaned_data
