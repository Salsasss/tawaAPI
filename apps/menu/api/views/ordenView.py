from rest_framework import viewsets
from apps.menu.models.Orden import Orden
from apps.menu.api.serializers.OrdenSerializer import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    """
    Endpoint para listar y crear órdenes.
    """
    serializer_class = OrdenSerializer
    queryset = Orden.objects.all()
    
    ordering_fields = ['created_at']
    ordering = ['-created_at']