from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.menu.api.views import (
    IngredienteViewSet,
    CategoriaProductoViewSet,
    ProductoViewSet,
    OrdenViewSet,
    DetalleOrdenViewSet
)

router = DefaultRouter()
router.register(r'ingredientes', IngredienteViewSet, basename='ingredientes')
router.register(r'categorias', CategoriaProductoViewSet, basename='categorias')
router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'ordenes', OrdenViewSet, basename='ordenes')
router.register(r'detalles-orden', DetalleOrdenViewSet, basename='detalles-orden')

urlpatterns = [
    path('', include(router.urls)),
]