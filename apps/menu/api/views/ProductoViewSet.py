from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.menu.models.Producto import Producto
from apps.menu.api.serializers.ProductoSerializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # Usamos prefetch_related y select_related para optimizar las consultas DB (N+1)
    queryset = Producto.objects.select_related('categoria').prefetch_related('ingredientes').all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['categoria', 'is_active']