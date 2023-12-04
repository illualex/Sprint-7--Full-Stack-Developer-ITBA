import os
print('mira aca')
import django

# Establece la ruta a tu proyecto Django y la configuración

                # ESTA LINEA ES LA QUE DA ERROR Y NO DEJA CORRER EL ARCHIVO
                
# # # # # # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bcib-sprint7.bcib_itba.bcib_itba.settings')


# print(os.environ.get('DJANGO_SETTINGS_MODULE'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configura Django
django.setup()

# Importa los modelos después de configurar Django
from django.contrib.auth.models import User
from cliente.models import Cliente 

# Accede a la base de datos SQLite y crea usuarios en Django
clientes = Cliente.objects.all()

# Contraseña predeterminada para todos los usuarios
contraseña_predeterminada = 'tu_contraseña_predeterminada'

for cliente in clientes:
    # Obtiene información del cliente
    first_name = cliente.customer_name
    last_name = cliente.customer_surname

    # Genera el username y el email
    username = ''.join(e for e in (first_name + last_name) if e.isalnum())
    email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"

    # Crea un nuevo usuario en Django
    nuevo_usuario = User.objects.create_user(
        id=cliente.id,
        username=username,
        email=email,
        password=contraseña_predeterminada,
        first_name=first_name,
        last_name=last_name,
    )

    # Vincula el cliente con el usuario creado
    cliente.usuario = nuevo_usuario
    cliente.save()