from django.urls import path
from api.apiviews import ProductoList, ProductoSave, ProductoDetalle, CategoriaSave, CategoriaList, SubCategoriaSave, SubCategoriaList

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name = 'producto_list'),
    path('v1/productos/add', ProductoSave.as_view(), name = 'producto_save'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name = 'producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name = 'categoria_list'),
    path('v1/categorias/add', CategoriaSave.as_view(), name = 'categoria_save'),
    path('v1/subcategorias/', SubCategoriaList.as_view(), name = 'subcategoria_list'),
    path('v1/subcategorias/add', SubCategoriaSave.as_view(), name = 'subcategoria_save')
]