
from rest_framework import serializers
from .models import SolicitudPrestamo

class SolicitudPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudPrestamo
        fields = '__all__'
