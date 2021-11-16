from rest_framework import serializers 
from .models import PQR, PersonaSoporte

class PersonaSoporteSerializar(serializers.ModelSerializer):
    class Meta:
        model = PersonaSoporte
        fields = '__all__'

class PQRSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = ['persona_soporte', 'estado', 'comentario']