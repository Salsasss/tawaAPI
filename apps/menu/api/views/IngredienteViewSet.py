from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.menu.models.Ingrediente import Ingrediente
from apps.menu.api.serializers.IngredienteSerializer import IngredienteSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]