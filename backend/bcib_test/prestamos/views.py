from .forms import SolicitudPrestamoForm
from .models import SolicitudPrestamo
from .serializers import SolicitudPrestamoSerializer
from django.shortcuts import render, redirect
from .forms import SolicitudPrestamoForm
from django.http import JsonResponse
from .models import Cliente, SolicitudPrestamo
from .forms import SolicitudPrestamoForm
# En el archivo views.py de la aplicación de préstamos
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SolicitudPrestamo
from .forms import LoanRequestForm

def cliente_detail(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    # Asegúrate de tener un método apropiado para serializar el cliente a JSON si es necesario
    cliente_data = {'id': cliente.id, 'nombre': cliente.nombre, 'tipo_cliente': cliente.tipo_cliente}
    return JsonResponse(cliente_data)

def crear_solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user.cliente 
            solicitud.monto_solicitado = solicitud.tipo_prestamo.monto_maximo  
            solicitud.save()

            aprobado = True  # Determina si la solicitud fue aprobada o rechazada (puede ser un booleano)
            return render(request, 'prestamos/solicitud_exitosa.html', {'mensaje': 'Su solicitud ha sido aprobada.'})  # o rechazada según aprobado

    else:
        form = SolicitudPrestamoForm()
    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})



# @login_required
# def loan_request_form(request):
#     if request.method == 'POST':
#         form = LoanRequestForm(request.POST)
#         if form.is_valid():
#             loan_req = form.save(commit=False)
#             loan_req.user = request.user  # Asignar el usuario autenticado
#             if loan_req.loan_type == 'BLACK' and loan_req.amount_requested > 500000:
#                 loan_req.approved = False
#             elif loan_req.loan_type == 'GOLD' and loan_req.amount_requested > 300000:
#                 loan_req.approved = False
#             elif loan_req.loan_type == 'CLASSIC' and loan_req.amount_requested > 100000:
#                 loan_req.approved = False
#             else:
#                 loan_req.approved = True  # La solicitud es aprobada

#             loan_req.save()  # Guardar la solicitud
#             return render(request, 'loan_confirmation.html', {'approved': loan_req.approved})
#     else:
#         form = LoanRequestForm()
    
    # return render(request, 'loan_request_form.html', {'form': form})

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

def solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user.cliente 
            solicitud.monto_solicitado = solicitud.tipo_prestamo.monto_maximo  
            solicitud.fecha_inicio=form.cleaned_data['fecha_inicio']
            solicitud.save()
            
            aprobado = True  # Determina si la solicitud fue aprobada o rechazada (puede ser un booleano)
            return redirect('prestamos/solicitud_exitosa.html', aprobado=aprobado)
    #OPERACIONES PARA QUE SE VEA REFLEJADO EN EL ESTADO DE CUENTA
        # Una vez solicitada la solicitud de préstamo, se debe registrar
        # en la base dedatos. La solicitud debe impactar en el préstamo y 
        # en el saldo de cuenta. Entodo momento, el formulario debe informar
        # si la solicitud fue aprobada orechazada
        
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})
