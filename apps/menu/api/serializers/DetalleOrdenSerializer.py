from rest_framework import serializers

from apps.menu.models.DetalleOrden import DetalleOrden
from apps.menu.api.serializers.ProductoSerializer import ProductoSerializer

class DetalleOrdenSerializer(serializers.ModelSerializer):
    producto_detalle = ProductoSerializer(source='producto', read_only=True)
    
    class Meta:
        model = DetalleOrden
        fields = ['id', 'producto', 'producto_detalle', 'cantidad', 'precio_unitario', 'notas', 'preparado']
        read_only_fields = ['precio_unitario'] # El precio se debería calcular/fijar en la Orden, pero lo podemos mandar
