from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.menu.models.CategoriaProducto import CategoriaProducto
from apps.menu.api.serializers.CategoriaProductoSerializer import CategoriaProductoSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]