from rest_framework import serializers
from django.db import transaction

from apps.menu.api.serializers.DetalleOrdenSerializer import DetalleOrdenSerializer

from apps.menu.models.Orden import Orden
from apps.menu.models.DetalleOrden import DetalleOrden

class OrdenSerializer(serializers.ModelSerializer):
    # Declaramos que la orden recibirá una lista de detalles
    detalles = DetalleOrdenSerializer(many=True)

    class Meta:
        model = Orden
        fields = ['id', 'mesa', 'estado', 'total', 'created_at', 'detalles']
        # Protegemos estos campos; el backend los calculará o asignará por defecto
        read_only_fields = ['total', 'created_at']

    def create(self, validated_data):
        # 1. Extraemos los detalles del payload
        detalles_data = validated_data.pop('detalles')
        
        # 2. transaction.atomic() asegura que si algo falla, no se guarde nada en la BD
        with transaction.atomic():
            # Creamos la orden inicial (el total por defecto es 0.00)
            orden = Orden.objects.create(**validated_data)
            total_calculado = 0
            
            # 3. Iteramos sobre cada ítem del carrito
            for detalle in detalles_data:
                producto = detalle['producto']
                cantidad = detalle['cantidad']
                
                # Obtenemos el precio real y seguro directamente del producto en BD
                precio_actual = producto.precio 
                
                # Creamos el registro del detalle de la orden
                DetalleOrden.objects.create(
                    orden=orden,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=precio_actual
                )
                
                # Vamos sumando al total de la orden
                total_calculado += (precio_actual * cantidad)
            
            # 4. Actualizamos el total final de la orden y guardamos
            # Nota: El IVA que muestras en tu diseño (16%) es puramente visual para el frontend,
            # el 'total_calculado' aquí ya incluye el precio final a pagar.
            orden.total = total_calculado
            orden.save()
            
        return orden