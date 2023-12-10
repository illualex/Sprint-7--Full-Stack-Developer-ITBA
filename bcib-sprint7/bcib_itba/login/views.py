from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('/perfil')  # Cambia 'inicio' por la URL a la que deseas redirigir después del inicio de sesión.
        else:
            messages.error(request, 'Credenciales incorrectas.')

    return render(request, 'login/login.html')  # Cambia 'login.html' por el nombre de tu plantilla de inicio de sesión.

def logout_view(request):
    logout(request)
    messages.success(request, 'Cierre de sesión exitoso.')
    return redirect('inicio')  # Cambia 'inicio' por la URL a la que deseas redirigir después del cierre de sesión.
