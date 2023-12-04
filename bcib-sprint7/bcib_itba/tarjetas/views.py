from django.shortcuts import render

# Create your views here.

def tarjetas_view(request):
    return render(request, 'tarjetas/tarjetas.html')