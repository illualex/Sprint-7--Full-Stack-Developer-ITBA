from django import forms
from .models import SolicitudPrestamo, TipoPrestamo, Cliente
from django.utils import timezone
from django.core.validators import MaxLengthValidator, RegexValidator
from django.contrib.auth.models import User
import random



class SolicitudPrestamoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
    label='Fecha de Inicio del Préstamo',
    input_formats=['%d/%m/%Y'],
    widget=forms.DateInput(attrs={'class': 'datepicker'}),
    help_text='Ingrese una fecha en formato dd/mm/aaaa y asegúrese de que no sea una fecha pasada.'
    )
    monto_solicitado = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d{1,14}$',
                message='El monto debe contener solo números.',
                code='invalid_monto'
            ),
            MaxLengthValidator(14, message='El monto no puede tener más de 14 dígitos.')
        ],
        widget=forms.TextInput(attrs={'pattern': '[0-9]{1,14}', 'title': 'Ingrese solo números'})
    )
    # cliente = forms.IntegerField()
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
            cliente_id = random.randint(1, 505)

            if cliente_id:
                try:
                     usuario = User.objects.get(id=cliente_id)
                     cliente = Cliente.objects.get(user=usuario)

                except (Cliente.DoesNotExist, User.DoesNotExist):
                    raise forms.ValidationError("Cliente no encontrado")

            else:
                raise forms.ValidationError("ID de cliente no proporcionado o no válido",cliente_id.__str__)

            return cleaned_data