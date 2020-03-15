from usuarios.views import *
from rest_framework.routers import DefaultRouter

app_name="usuarios"

router = DefaultRouter()
router.register(r'users', UserViewSet,'usuarios')
router.register(r'cities', CityViewSet,'cities')
router.register(r'profiles', ProfileViewSet,'profiles')
