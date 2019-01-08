from rest_framework import serializers
from .models import inmueble, general, interior, exterior

class inmueble_S(serializers.ModelSerializer):
    class Meta:
        model = inmueble
        fields = ('url', 'id', 'tipo', 'subtipo', 'gen', 'inte', 'ext')

class generalSerializer(serializers.ModelSerializer):
    class Meta:
        model = general
        fields = ('url', 'id', 'direccion', 'ciudad', 'departamento', 'pais', 'telefono')

class interiorSerializer(serializers.ModelSerializer):
    class Meta:
        model = interior
        fields = ('url', 'id', 'cuartos', 'baños', 'closets', 'calentador')

class exteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = exterior
        fields = ('url', 'id', 'vigilancia', 'parqueadero', 'salon_social', 'numero_pisos')
