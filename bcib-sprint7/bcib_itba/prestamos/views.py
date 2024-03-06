from django.shortcuts import render, redirect
from .forms import SolicitudPrestamoForm
from cliente.models import Cliente
from .models import SolicitudPrestamo
from django.contrib.auth.decorators import login_required
from random import randint
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
# from home.views import home_view
from django.urls import reverse


@login_required
@csrf_protect
def prestamos_view(request):
    try:
        if request.user.is_authenticated:
            cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
          return redirect(reverse('login'))


    cliente_id_aleatorio = randint(1, 505)
    try:
        usuario = User.objects.get(id=cliente_id_aleatorio)
        cliente_aleatorio = Cliente.objects.get(user=usuario)
    except Cliente.DoesNotExist:
        cliente_aleatorio = Cliente.objects.get(user=2)  

    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = cliente if cliente else cliente_aleatorio
            solicitud.aprobado = True 
            solicitud.save()

            if solicitud.aprobado == True:
                mensaje = "Solicitud de préstamo aprobada"
                aprobado = True
                # Actualizar el monto de saldo en cuenta 
            else:
                mensaje = "Solicitud de préstamo rechazada"
                aprobado = False

            return render(request, 'prestamos/resultado_solicitud.html', {'aprobado': aprobado, 'mensaje': mensaje})
    else:
        form = SolicitudPrestamoForm()

    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})
