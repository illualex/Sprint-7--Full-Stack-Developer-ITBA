from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def perfil_view(request):
    print(f"¿El usuario está autenticado? {request.user.is_authenticated}")
    return render(request, 'perfil/perfil.html')

