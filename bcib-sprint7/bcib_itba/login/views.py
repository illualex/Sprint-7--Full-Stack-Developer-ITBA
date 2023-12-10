from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .serializers import AuthUserSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')

            # Serializar el usuario autenticado
            serializer = AuthUserSerializer(user)
            serialized_user = serializer.data

            # Puedes acceder a los datos serializados en serialized_user
            print(serialized_user)

            return redirect('/perfil')  # Reemplaza '/perfil' con la URL a la que deseas redirigir después del inicio de sesión.
        else:
            messages.error(request, 'Credenciales incorrectas.')
            
    
    return render(request, 'login/login.html')
