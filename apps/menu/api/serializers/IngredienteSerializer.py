from rest_framework import serializers
from apps.menu.models.Ingrediente import Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre']
