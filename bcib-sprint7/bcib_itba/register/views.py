from django.shortcuts import render
from cliente.models import Cliente

# Create your views here.
def register_view(request):

    return render(request, 'register/register.html')