from django import forms;
from .models import SolicitudPrestamo

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = SolicitudPrestamo
        fields = ['monto_solicitado','tipo_prestamo', 'fecha_inicio']
        
    def clean(self):
        cleaned_data = super().clean()
        # tipo_prestamo = cleaned_data.get('tipo_prestamo')
        cliente = cleaned_data.get('cliente')
        monto_solicitado = forms.DecimalField(label='Monto del Préstamo')
        tipo_prestamo = forms.ModelChoiceField(queryset=TipoPrestamo.objects.all(), label='Tipo de Préstamo')
        fecha_inicio = forms.DateField(label='Fecha de Inicio del Préstamo')
    

        if cliente.tipoCliente =='BLACK':
            tipo_prestamo.monto_maximo=500000
        elif cliente.tipoCliente =='GOLD':
            tipo_prestamo.monto_maximo=300000
        else:
            tipo_prestamo.monto_maximo=100000

        # Ejemplo de validación de monto máximo
        if tipo_prestamo and cliente:
            if tipo_prestamo.monto_maximo < monto_solicitado:
                raise forms.ValidationError("El monto solicitado supera el límite para este tipo de préstamo")
        return cleaned_data
    
