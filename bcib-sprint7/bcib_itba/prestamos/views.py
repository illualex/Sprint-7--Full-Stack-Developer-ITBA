from django.shortcuts import render,get_object_or_404
from .forms import SolicitudPrestamoForm
from cliente.models import  Cliente
from .models import SolicitudPrestamo, Prestamo
from django.contrib.auth.decorators import login_required
from random import randint
from django.contrib.auth.models import User

@login_required
def prestamos_view(request):
    # # cliente = get_object_or_404(Cliente, user=request.user)
    # try:
    #     cliente = Cliente.objects.get(user=request.user)
    # except Cliente.DoesNotExist:
    #     # Manejar el caso en el que no se encuentra el cliente
    #     cliente = None  # O cualquier otro manejo de la situación
    #     return render(request, '404.html')
    # cliente= obtener_cliente_por_usuario(request.user)
    cliente_id_aleatorio = randint(1, 505)
    try:
        usuario = User.objects.get(id=cliente_id_aleatorio)
        cliente = Cliente.objects.get(user=usuario)
    except Cliente.DoesNotExist:
        cliente = Cliente.objects.get(user=2)
        # Leslie
    if request.method == 'POST':
        # form = SolicitudPrestamoForm(request.POST,initial={'cliente': cliente_id_aleatorio})
        form = SolicitudPrestamoForm(request.POST)
        print('ENTRO POST')
        if form.is_valid():
            print('ENTRO AL FORM IS VALID')
            solicitud = form.save(commit=False)
            solicitud.cliente = cliente
            solicitud.aprobado = True  # Aquí debes realizar la lógica de aprobación o rechazo
            solicitud.save()

            # Actualizar el préstamo y el saldo de cuenta aquí

            
            if solicitud.aprobado==True:
                mensaje = "Solicitud de préstamo aprobada"
                aprobado = True
            else:
                mensaje = "Solicitud de préstamo rechazada"
                aprobado = False

            return render(request, 'prestamos/resultado_solicitud.html', {'aprobado': aprobado, 'mensaje': mensaje})
    else:
        form = SolicitudPrestamoForm()

    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})
