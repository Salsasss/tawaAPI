from django.db import models
from django.core.validators import MinValueValidator

from apps.menu.models.Orden import Orden
from apps.menu.models.Producto import Producto

class DetalleOrden(models.Model):
    orden = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE,
        related_name='detalles',
        verbose_name="Orden"
    )
    
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT, # No permite borrar el producto si ya está en una orden
        verbose_name="Producto"
    )
    
    cantidad = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Cantidad"
    )
    
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Precio Unitario",
        help_text="Precio al que se vendió para evitar cambios históricos"
    )

    class Meta:
        verbose_name = "Detalle de Orden"
        verbose_name_plural = "Detalles de Órdenes"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Orden {self.orden.id})"