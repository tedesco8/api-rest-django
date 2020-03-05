from contenedores.views import ContenedorViewSet
from rest_framework.routers import DefaultRouter

app_name="contenedores"

router = DefaultRouter()
router.register(r'contenedores', ContenedorViewSet,'contenedores')
