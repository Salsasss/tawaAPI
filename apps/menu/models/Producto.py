from django.db import models
from django.core.validators import MinValueValidator

from apps.menu.models import CategoriaProducto

class Producto(models.Model):
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre del Producto",
        help_text="Nombre comercial del platillo"
    )
    
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Detalles del platillo"
    )
    
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio",
        help_text="Precio en Pesos(MXN)"
    )
    
    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True,
        verbose_name="Imagen del producto"
    )
    
    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.CASCADE,
        related_name='productos',
        verbose_name="Categoría",
        db_index=True # Indexado para filtrar rápido por categoría en el menú
    )
    
    is_active = models.BooleanField(
        default=True,
        db_index=True, # Indexado para mostrar solo lo que hay en existencia
        verbose_name="Disponible",
        help_text="Desmarcar si el producto se agotó"
    )
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre