from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

'''
class CRideModel(models.Model):
    created = models.DateTimeField(
        'created at',
        auto_now_add = True,
        help_text = 'Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text = 'Date time on which the object was last created.'
    )
    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

'''

class Contenedor(models.Model):
    colaborador = models.ForeignKey (
        User, on_delete=models.SET_NULL, 
        null = True, 
        blank = True
    )
    descripcion = models.CharField (
        max_length = 100,
        help_text = 'Descripción del Contenedor',
        unique = True
    )
    
    activo = models.BooleanField (
        default = False
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
        null = True,
        blank=True
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