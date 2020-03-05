from usuarios.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name="usuarios"

router = DefaultRouter()
router.register(r'users', UserViewSet,'usuarios')
