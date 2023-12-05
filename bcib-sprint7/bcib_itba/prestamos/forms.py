from django import forms
from .models import SolicitudPrestamo, TipoPrestamo, Cliente
from django.utils import timezone

class SolicitudPrestamoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
    label='Fecha de Inicio del Préstamo',
    input_formats=['%d/%m/%Y'],
    widget=forms.DateInput(attrs={'class': 'datepicker'}),
    help_text='Ingrese una fecha en formato dd/mm/aaaa y asegúrese de que no sea una fecha pasada.'
    )
    class Meta:
        model = SolicitudPrestamo
        fields = ['monto_solicitado', 'tipo_prestamo', 'fecha_inicio']
    
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio < timezone.now().date():
            raise forms.ValidationError('La fecha no puede ser en el pasado.')
        return fecha_inicio

    def clean(self):
        cleaned_data = super().clean()
        cliente = None

        # Verificar si la instancia tiene un cliente asociado
        if 'cliente' in self.cleaned_data:
            cliente = self.cleaned_data['cliente']
        # elif self.instance.cliente:
        #     cliente = Cliente.objects.get(user=self.instance.cliente.user)
        else:
            cliente = Cliente.objects.get(user=2)
        
        # Realizar las operaciones que necesites con el objeto cliente aquí
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