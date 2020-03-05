from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from usuarios.userViews import UserCreate

urlpatterns = [
    path("v2/token/", jwt_views.TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('v2/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('v2/user/', UserCreate.as_view(), name='user_create'),
]