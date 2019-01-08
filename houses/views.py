from .models import inmueble, general, interior, exterior
from .serializers import inmueble_S, generalSerializer, interiorSerializer, exteriorSerializer
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

class inmuebleViewSet(viewsets.ModelViewSet):
    queryset = inmueble.objects.all()
    serializer_class = inmueble_S

class generalViewSet(viewsets.ModelViewSet):
    queryset = general.objects.all()
    serializer_class = generalSerializer

class interiorViewSet(viewsets.ModelViewSet):
    queryset = interior.objects.all()
    serializer_class = interiorSerializer

class exteriorViewSet(viewsets.ModelViewSet):
    queryset = exterior.objects.all()
    serializer_class = exteriorSerializer
