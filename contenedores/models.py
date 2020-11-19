from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Contenedor(models.Model):
    colaborador = models.ForeignKey (
        User, 
        on_delete=models.SET_NULL, 
        null = True, 
        blank = True
    )
    descripcion = models.CharField (
        max_length = 100,
        help_text = 'Descripción del Contenedor',
        unique = True
    )
    
    activo = models.BooleanField (
        default = True
    )

    created = models.DateTimeField (
        'created at',
        auto_now_add = True,
        help_text = 'Date time on which the object was created.'
    )
    modified = models.DateTimeField (
        'modified at',
        auto_now = True,
        help_text = 'Date time on which the object was last created.'
    )

    weight = models.FloatField (
        default = 0,
        help_text = 'Peso del Contenedor'
    )

    lat = models.FloatField (
        default = 0,
        blank = True,
        null = True
    )
    lng = models.FloatField (
        default = 0,
        blank = True,
        null = True
    )

 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Contenedores"