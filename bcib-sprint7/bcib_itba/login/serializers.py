from rest_framework import serializers
from .models import AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'password']

    # Asegúrate de establecer el campo de contraseña como de escritura (write-only)
    password = serializers.CharField(write_only=True)
