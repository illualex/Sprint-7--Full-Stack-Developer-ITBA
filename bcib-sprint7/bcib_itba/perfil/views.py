from django.shortcuts import render

# Create your views here.
def perfil_view(request):
    return render(request, 'perfil/perfil.html')