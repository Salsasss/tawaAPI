from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.menu.models.Orden import Orden
from apps.menu.api.serializers.OrdenSerializer import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.prefetch_related('detalles', 'detalles__producto').all()
    serializer_class = OrdenSerializer
    filterset_fields = ['estado', 'mesa', 'es_para_llevar']

    def get_permissions(self):
        """
        Permite a clientes anonimos crear ordenes (POST).
        Para cualquier otra accion (GET, PUT, PATCH, DELETE) requiere autenticacion de empleado.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]