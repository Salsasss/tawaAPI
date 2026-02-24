from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.menu.models.Producto import Producto

from apps.menu.api.serializers.ProductoSerializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = ProductoSerializer.Meta.model.objects.filter(is_active=True)
    
    # Habilitamos el backend de filtros
    filter_backends = [DjangoFilterBackend]
    
    # ¡Magia! DRF habilitará automáticamente /?categoria=X y /?es_popular=true
    filterset_fields = ['categoria']