from django.urls import path
from .views import categoria_list, categoria_detalle

urlpatterns = [
    path('categorias/', categoria_list, name='categoria_list'),
    path('categorias/<int:pk>', categoria_detalle, name='categoria_detalle')
]