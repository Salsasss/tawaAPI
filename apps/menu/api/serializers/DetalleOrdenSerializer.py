from rest_framework import serializers
from apps.menu.models.DetalleOrden import DetalleOrden

class DetalleOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrden
        # El frontend solo nos enviará 'ID de producto' y 'cantidad'.
        fields = ['producto', 'cantidad', 'precio_unitario']
        # Bloqueamos el precio_unitario para que el frontend no pueda inyectarlo
        read_only_fields = ['precio_unitario']