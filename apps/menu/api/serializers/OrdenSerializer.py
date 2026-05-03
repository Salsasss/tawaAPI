from rest_framework import serializers

from apps.menu.models.Orden import Orden
from apps.menu.models.DetalleOrden import DetalleOrden
from apps.menu.models.Producto import Producto
from apps.menu.api.serializers.DetalleOrdenSerializer import DetalleOrdenSerializer

class OrdenSerializer(serializers.ModelSerializer):
    detalles = DetalleOrdenSerializer(many=True)
    
    class Meta:
        model = Orden
        fields = ['id', 'mesa', 'es_para_llevar', 'metodo_pago', 'subtotal', 'iva', 'propina', 'total', 'created_at', 'estado', 'detalles']
        read_only_fields = ['subtotal', 'iva', 'total', 'created_at']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles', [])
        propina = validated_data.get('propina', 0)
        
        orden = Orden.objects.create(**validated_data)
        
        subtotal = 0
        for detalle_data in detalles_data:
            producto = detalle_data['producto']
            cantidad = detalle_data.get('cantidad', 1)
            notas = detalle_data.get('notas', '')
            
            # Tomamos el precio actual del producto
            precio_unitario = producto.precio
            subtotal += precio_unitario * cantidad
            
            DetalleOrden.objects.create(
                orden=orden,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                notas=notas
            )
            
        # Calcular impuestos y total final
        iva = float(subtotal) * 0.16
        total_final = float(subtotal) + iva + float(propina)
        
        orden.subtotal = subtotal
        orden.iva = iva
        orden.total = total_final
        orden.save()
        
        return orden