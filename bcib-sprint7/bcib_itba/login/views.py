from django.shortcuts import render
from cliente.models import Cliente

# Create your views here.

def login_view(request):
    
    return render(request, 'login/login.html')
