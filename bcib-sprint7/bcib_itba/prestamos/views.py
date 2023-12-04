# from django.shortcuts import render
# from .forms import SolicitudPrestamoForm


# def prestamos_view(request):
#     if request.method == 'POST':
#         form = SolicitudPrestamoForm(request.POST)
#         if form.is_valid():
#             # Procesar la solicitud de préstamo
#             solicitud = form.save(commit=False)
#             # Realizar lógica de negocios y registro en la base de datos aquí
#             solicitud.save()
#     else:
#         form = SolicitudPrestamoForm()

#     return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})

from django.shortcuts import render
from .forms import SolicitudPrestamoForm
from .models import SolicitudPrestamo, Prestamo, Cliente

def prestamos_view(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = Cliente.objects.get(user=request.user)
            solicitud.aprobado = True  # Aquí debes realizar la lógica de aprobación o rechazo
            solicitud.save()

            # Actualizar el préstamo y el saldo de cuenta aquí

            
            if solicitud.aprobado:
                mensaje = "Solicitud de préstamo aprobada"
            else:
                mensaje = "Solicitud de préstamo rechazada"

            return render(request, 'resultado_solicitud.html', {'mensaje': mensaje})
    else:
        form = SolicitudPrestamoForm()

    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})
