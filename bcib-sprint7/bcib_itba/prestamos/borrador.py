from .forms import SolicitudPrestamoForm
from .serializers import SolicitudPrestamoSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cliente, SolicitudPrestamo
from django.contrib.auth.decorators import login_required
from cliente import Cliente

def cliente_detail(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    # Asegúrate de tener un método apropiado para serializar el cliente a JSON si es necesario
    cliente_data = {'id': cliente.id, 'nombre': cliente.nombre, 'tipo_cliente': cliente.tipo_cliente}
    return JsonResponse(cliente_data)

@login_required
def solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user.cliente 
            if solicitud.loan_type == 'BLACK' and solicitud.amount_requested > 500000:
                solicitud.approved = False
            elif solicitud.loan_type == 'GOLD' and solicitud.amount_requested > 300000:
                solicitud.approved = False
            elif solicitud.loan_type == 'CLASSIC' and solicitud.amount_requested > 100000:
                solicitud.approved = False
            else:
                solicitud.approved = True  # La solicitud es aprobada
            # solicitud.monto_solicitado = solicitud.tipo_prestamo.monto_maximo  
            solicitud.save()
             #OPERACIONES PARA QUE SE VEA REFLEJADO EN EL ESTADO DE CUENTA
                # Una vez solicitada la solicitud de préstamo, se debe registrar
                # en la base dedatos. La solicitud debe impactar en el préstamo y 
                # en el saldo de cuenta. Entodo momento, el formulario debe informar
                # si la solicitud fue aprobada orechazada
            return render(request, 'prestamos/solicitud_exitosa.html', {'mensaje': 'Su solicitud ha sido aprobada.'})  # o rechazada según aprobado
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})




def lista_solicitudes_prestamo_cliente(request, cliente_id):
    solicitudes = SolicitudPrestamo.objects.filter(cliente__id=cliente_id)
    # Asegúrate de tener un método apropiado para serializar las solicitudes a JSON si es necesario
    solicitudes_data = [{'id': solicitud.id, 'monto_solicitado': solicitud.monto_solicitado} for solicitud in solicitudes]
    return JsonResponse({'solicitudes': solicitudes_data})


# def mi_vista_personalizada(request):
#     # Lógica de la vista
#     return render(request, 'prestamos/tu_template.html')  # Ruta correcta a la plantilla


def solicitud_exitosa(request, aprobado):
    mensaje = "Su solicitud ha sido aprobada." if aprobado else "Su solicitud ha sido rechazada."
    return render(request, 'prestamos/solicitud_exitosa.html', {'mensaje': mensaje})

   

@login_required
def prestamos_view(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            # Realizar lógica de negocios y validaciones adicionales aquí
            solicitud.save()
            return render(request, 'solicitud_aprobada.html', {'solicitud': solicitud})
        else:
            # El formulario no es válido, se debe renderizar con los errores
            return render(request, 'prestamos.html', {'form': form})
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'solicitud_prestamo.html', {'form': form})



def solicitar_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            # Procesar la solicitud de préstamo
            solicitud = form.save(commit=False)
            # Realizar lógica de negocios y registro en la base de datos aquí
            solicitud.save()
            return render(request, 'solicitud_aprobada.html', {'solicitud': solicitud})
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})


