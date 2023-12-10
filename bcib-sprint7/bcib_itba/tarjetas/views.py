from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cliente.models import Cliente

@login_required
def tarjetas_view(request):
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
    return render(request, 'tarjetas/tarjetas.html')

# from django.shortcuts import render
# from .models import Tarjeta  # Reemplaza 'Tarjeta' con el nombre de tu modelo

# def mostrar_tarjetas(request):
#     tarjetas = Tarjeta.objects.all()  # Obtén todas las tarjetas de la base de datos
#     return render(request, 'nombre_tu_template.html', {'tarjetas': tarjetas})
