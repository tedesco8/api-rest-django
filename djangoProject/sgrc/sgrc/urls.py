from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from contenedores.urls import router as contenedores_router
from usuarios.urls import router as usuarios_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path("v2/login/", jwt_views.TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('v2/login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    
    #path('api/contenedores/', include(contenedores_router.urls,namespace='contenedores')),
    #path('api/usuarios/', include(usuarios_router.urls,namespace='usuarios'))

    path('api/contenedores/', include((contenedores_router.urls,'contenedores'))),
    path('api/usuarios/', include((usuarios_router.urls,'usuarios')))
]

#urlpatterns += router.urls