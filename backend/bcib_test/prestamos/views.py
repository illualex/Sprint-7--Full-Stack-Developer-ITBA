from django.shortcuts import render, redirect
from .models import SolicitudPrestamo
from .forms import SolicitudPrestamoForm


def solicitud_exitosa(request, aprobado):
    mensaje = "Su solicitud ha sido aprobada." if aprobado else "Su solicitud ha sido rechazada."
    return render(request, 'solicitud_exitosa.html', {'mensaje': mensaje})

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
            return redirect('solicitud_exitosa', aprobado=aprobado)
    #OPERACIONES PARA QUE SE VEA REFLEJADO EN EL ESTADO DE CUENTA
        # Una vez solicitada la solicitud de préstamo, se debe registrar
        # en la base dedatos. La solicitud debe impactar en el préstamo y 
        # en el saldo de cuenta. Entodo momento, el formulario debe informar
        # si la solicitud fue aprobada orechazada
        
    else:
        form = SolicitudPrestamoForm()
    return render(request, 'solicitud_prestamo.html', {'form': form})

