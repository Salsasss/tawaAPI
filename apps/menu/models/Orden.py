from django.db import models

from apps.menu.utils import ESTADOS_ORDEN

class Orden(models.Model):
    mesa = models.PositiveIntegerField(
        verbose_name="Número de Mesa",
        help_text="Mesa que realiza el pedido"
    )
    
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Total de la Orden"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True, # index -> Útil para ordenar por las más recientes o reportes diarios
        verbose_name="Fecha de Creación"
    )
    
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_ORDEN,
        default='NUEVA',
        db_index=True, # index -> Para que la pantalla del empleado cargue las columnas rápido
        verbose_name="Estado de la Orden",
        help_text="Determina en qué columna aparece la orden para el empleado"
    )
    
    para_llevar = models.BooleanField(
        default=False,
        verbose_name="Para llevar",
        help_text="El pedido es para llevar"
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-created_at']

    def __str__(self):
        return f"Orden {self.id} - Mesa {self.mesa}"