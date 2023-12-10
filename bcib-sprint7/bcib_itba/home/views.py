from django.shortcuts import render
from cliente.models import Cliente

# Create your views here.


def home_view(request):
    
    return render(request, 'home/home.html')
