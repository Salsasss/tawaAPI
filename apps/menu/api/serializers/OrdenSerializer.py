from rest_framework import serializers

from apps.menu.models.Orden import Orden
from apps.menu.models.DetalleOrden import DetalleOrden
from apps.menu.models.Producto import Producto
from apps.menu.api.serializers.DetalleOrdenSerializer import DetalleOrdenSerializer

class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True)
    
    class Meta:
        model = Orden
        fields = ['id', 'mesa', 'es_para_llevar', 'total', 'created_at', 'estado', 'detalles']
        read_only_fields = ['total', 'created_at']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        
        # El total lo podemos calcular aquí si no se pasa del frontend
        # o dejarlo en 0 y sumarlo despues de agregar los detalles
        orden = Orden.objects.create(**validated_data)
        
        total = 0
        for detalle_data in detalles_data:
            producto = detalle_data['producto']
            cantidad = detalle_data.get('cantidad', 1)
            notas = detalle_data.get('notas', '')
            
            # Tomamos el precio actual del producto
            precio_unitario = producto.precio
            total += precio_unitario * cantidad
            
            DetalleOrden.objects.create(
                orden=orden,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                notas=notas
            )
            
        orden.total = total
        orden.save()
        
        return orden
