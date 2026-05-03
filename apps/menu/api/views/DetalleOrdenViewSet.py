from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.menu.models.DetalleOrden import DetalleOrden
from apps.menu.api.serializers.DetalleOrdenSerializer import DetalleOrdenSerializer

class DetalleOrdenViewSet(viewsets.ModelViewSet):
    queryset = DetalleOrden.objects.all()
    serializer_class = DetalleOrdenSerializer
    permission_classes = [IsAuthenticated] # Solo el KDS/Empleados deberían cambiar esto
