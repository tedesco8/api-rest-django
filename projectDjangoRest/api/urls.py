from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.apiviews import ProductoList, ProductoSave, ProductoDetalle, CategoriaSave, CategoriaList, CategoriaDetalle, SubCategoriaSave, SubCategoriaList, UserCreate, ProductoViewSet, LoginView

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name = 'producto_list'),
    path('v1/productos/add', ProductoSave.as_view(), name = 'producto_save'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name = 'producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name = 'categoria_list'),
    path('v1/categorias/add', CategoriaSave.as_view(), name = 'categoria_save'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
    path('v1/subcategorias/', SubCategoriaList.as_view(), name = 'subcategoria_list'),
    path('v1/categorias/<int:pk>/subcategorias/<int:cat_pk>/add', SubCategoriaSave.as_view(), name = 'subcategoria_save'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list'),
    path('v3/user/', UserCreate.as_view(), name='user_create'),
    path('v4/login', LoginView.as_view(), name='login'),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
]

urlpatterns += router.urls