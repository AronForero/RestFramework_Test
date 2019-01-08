from rest_framework import serializers
from .models import inmueble, general, interior, exterior

class inmueble_S(serializers.ModelSerializer):
    """
    Serializador para nuestro modelo principal
    """
    class Meta:
        model = inmueble #Se indica el modelo
        fields = ('url', 'id', 'tipo', 'subtipo', 'gen', 'inte', 'ext') #Se indican los campos que se van a mostrar en el json

class generalSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo general
    """
    class Meta:
        model = general
        fields = ('url', 'id', 'direccion', 'ciudad', 'departamento', 'pais', 'telefono')

class interiorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo interior
    """
    class Meta:
        model = interior
        fields = ('url', 'id', 'cuartos', 'baños', 'closets', 'calentador')

class exteriorSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo exterior
    """
    class Meta:
        model = exterior
        fields = ('url', 'id', 'vigilancia', 'parqueadero', 'salon_social', 'numero_pisos')
