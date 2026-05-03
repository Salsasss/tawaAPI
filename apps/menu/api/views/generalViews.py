from rest_framework import viewsets

from apps.menu.api.serializers.CategoriaProductoSerializer import CategoriaProductoSerializer

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaProductoSerializer
    queryset = CategoriaProductoSerializer.Meta.model.objects.all()