from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cliente.models import Cliente


@login_required
# Create your views here.
def perfil_view(request):
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
    return render(request, 'perfil/perfil.html')