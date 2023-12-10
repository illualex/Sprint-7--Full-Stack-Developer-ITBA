from django.shortcuts import render
from cliente.models import Cliente

# Create your views here.
def data_view(request):
    if request.user.is_authenticated:
        cliente = Cliente.objects.get(user=request.user)
    return render(request, "personal_data/personal_data.html")