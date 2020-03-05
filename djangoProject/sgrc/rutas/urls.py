from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from usuarios.userViews import UserCreate
from contenedores.containerViews import ContenedorViewSet

router = DefaultRouter()
router.register('v3/contenedor', ContenedorViewSet, basename='contenedor')

urlpatterns = [
    path("v2/login/", jwt_views.TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('v2/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('v2/user/', UserCreate.as_view(), name='user_create'),
]

urlpatterns += router.urls