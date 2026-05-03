from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del Ingrediente",
        help_text="Ej. Cebolla, Tomate, Sal"
    )

    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.nombre