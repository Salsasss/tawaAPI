from rest_framework import serializers

from apps.menu.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'is_active')