from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.menu.models.CategoriaProducto import CategoriaProducto
from apps.menu.api.serializers.CategoriaProductoSerializer import CategoriaProductoSerializer

class CategoriaProductoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura. Solo expone GET /categorias/ y GET /categorias/<id>/
    """
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [AllowAny]