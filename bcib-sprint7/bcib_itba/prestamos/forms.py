# from django import forms
# from .models import SolicitudPrestamo, TipoPrestamo, Cliente
# from django.utils import timezone
# from django.core.validators import MaxLengthValidator, RegexValidator


# class SolicitudPrestamoForm(forms.ModelForm):
#     fecha_inicio = forms.DateField(
#     label='Fecha de Inicio del Préstamo',
#     input_formats=['%d/%m/%Y'],
#     widget=forms.DateInput(attrs={'class': 'datepicker'}),
#     help_text='Ingrese una fecha en formato dd/mm/aaaa y asegúrese de que no sea una fecha pasada.'
#     )
#     monto_solicitado = forms.CharField(
#         validators=[
#             RegexValidator(
#                 regex=r'^\d{1,14}$',
#                 message='El monto debe contener solo números.',
#                 code='invalid_monto'
#             ),
#             MaxLengthValidator(14, message='El monto no puede tener más de 14 dígitos.')
#         ],
#         widget=forms.TextInput(attrs={'pattern': '[0-9]{1,14}', 'title': 'Ingrese solo números'})
#     )
#     class Meta:
#         model = SolicitudPrestamo
#         fields = ['monto_solicitado', 'tipo_prestamo', 'fecha_inicio','aprobado']
    
#     def clean_fecha_inicio(self):
#         fecha_inicio = self.cleaned_data.get('fecha_inicio')
#         if fecha_inicio < timezone.now().date():
#             raise forms.ValidationError('La fecha no puede ser en el pasado.')
#         return fecha_inicio

#     def clean(self):
#         cleaned_data = super().clean()
#         cliente = None

#         # Verificar si la instancia tiene un cliente asociado
#         if 'cliente' in self.cleaned_data:
#             cliente = self.cleaned_data['cliente']
#         # elif self.instance.cliente:
#         #     cliente = Cliente.objects.get(user=self.instance.cliente.user)
#         else:
#             cliente = Cliente.objects.get(user=2)
#             print('el cliente id es:',cliente.__str__)
#             # el username del cliente 2 es LeslieMoses
        
#         # Realizar las operaciones que necesites con el objeto cliente aquí
#         monto_solicitado = cleaned_data.get('monto_solicitado')
#         tipo_prestamo = cleaned_data.get('tipo_prestamo')

#         # Establecer los límites de préstamo según el tipo de cliente
#         if cliente.tipo_cliente == 'BLACK':
#             max_monto = 500000
#         elif cliente.tipo_cliente == 'GOLD':
#             max_monto = 300000
#         else:
#             max_monto = 100000

#         # Validar si el monto solicitado supera el límite para este tipo de préstamo
#         # monto_solicitado_int= (int)
#         if int(monto_solicitado) > max_monto:
#             raise forms.ValidationError("El monto solicitado supera el límite para este tipo de cliente")

#         return cleaned_data

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
    cliente = forms.IntegerField()
    class Meta:
        model = SolicitudPrestamo
        fields = ['monto_solicitado', 'tipo_prestamo', 'fecha_inicio','cliente']
    
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

                    # Resto del código de validación y lógica con el cliente obtenido

                except (Cliente.DoesNotExist, User.DoesNotExist):
                    raise forms.ValidationError("Cliente no encontrado")

            else:
                raise forms.ValidationError("ID de cliente no proporcionado o no válido",cliente_id.__str__)

            return cleaned_data