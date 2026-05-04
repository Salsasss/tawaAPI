from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.menu.models.Ingrediente import Ingrediente
from apps.menu.api.serializers.IngredienteSerializer import IngredienteSerializer

class IngredienteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [AllowAny]