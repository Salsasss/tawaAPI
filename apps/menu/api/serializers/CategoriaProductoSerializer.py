from rest_framework import serializers

from apps.menu.models import CategoriaProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ('nombre', )
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }