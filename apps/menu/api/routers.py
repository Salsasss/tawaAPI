from rest_framework.routers import DefaultRouter

from apps.menu.api.views.generalViews import CategoriaProductoViewSet
from apps.menu.api.views.productosView import ProductoViewSet
from apps.menu.api.views.ordenView import OrdenViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')
router.register(r'categoriaProductos', CategoriaProductoViewSet, basename='categoriaProductos')
router.register(r'ordenes', OrdenViewSet, basename='ordenes')

urlpatterns = router.urls