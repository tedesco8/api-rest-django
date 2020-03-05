from django.db import models
from django.conf import settings

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
class OwnerModel (models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class  Meta:
        abstract=True

class Contenedor(OwnerModel):
    colaborador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Contenedor',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    activo = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Contenedores"