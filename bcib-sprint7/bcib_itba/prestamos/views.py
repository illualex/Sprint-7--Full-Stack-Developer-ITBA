from django.shortcuts import render,get_object_or_404
from .forms import SolicitudPrestamoForm
from cliente.models import  Cliente
from .models import SolicitudPrestamo, Prestamo
from django.contrib.auth.decorators import login_required
from random import randint
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


@login_required
@csrf_protect
def prestamos_view(request):
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
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = cliente
            solicitud.aprobado = True  
            solicitud.save()

            # Actualizar el préstamo y el saldo de cuenta 

            
            if solicitud.aprobado==True:
                mensaje = "Solicitud de préstamo aprobada"
                aprobado = True
                # aca hay quue actualizar el monto de saldo en cuenta
            else:
                mensaje = "Solicitud de préstamo rechazada"
                aprobado = False

            return render(request, 'prestamos/resultado_solicitud.html', {'aprobado': aprobado, 'mensaje': mensaje})
    else:
        form = SolicitudPrestamoForm()

    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})
