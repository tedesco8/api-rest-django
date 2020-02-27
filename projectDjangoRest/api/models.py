from django.db import models
from django.conf import settings

# Django models utilities

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

# Create your models here
class Categoria(OwnerModel):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la Categoria',
        unique = True
    )
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    class Meta:
        verbose_name_plural = 'Categorias'

class SubCategoria(OwnerModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
    )
 
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
 
    class Meta:
        verbose_name_plural = "Sub Categorías"
        unique_together = ('categoria','descripcion')
 
 
class Producto(OwnerModel):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Productos"