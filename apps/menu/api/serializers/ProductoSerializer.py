from rest_framework import serializers

from apps.menu.models.Producto import Producto
from apps.menu.api.serializers.CategoriaProductoSerializer import CategoriaProductoSerializer
from apps.menu.api.serializers.IngredienteSerializer import IngredienteSerializer

class ProductoSerializer(serializers.ModelSerializer):
    # Campos anidados para lectura
    categoria_detalle = CategoriaProductoSerializer(source='categoria', read_only=True)
    ingredientes_detalle = IngredienteSerializer(source='ingredientes', many=True, read_only=True)
    
    class Meta:
        model = Producto
        fields = (
            'id', 'nombre', 'descripcion', 'precio', 'imagen', 
            'categoria', 'categoria_detalle', 
            'is_active', 'ingredientes', 'ingredientes_detalle'
        )