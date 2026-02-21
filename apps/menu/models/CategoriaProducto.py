from django.db import models
from django.core.validators import MinValueValidator

class CategoriaProducto(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre de la Categoría",
        help_text="Ejemplo: Platillos, Bebidas, Postres"
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre