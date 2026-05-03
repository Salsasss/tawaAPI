from rest_framework import serializers
from apps.menu.models.CategoriaProducto import CategoriaProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre']
