from contenedores.views import ContenedorViewSet, CoordenadasList
from rest_framework.routers import DefaultRouter
app_name="contenedores"

router = DefaultRouter()
router.register(r'contenedores', ContenedorViewSet,'contenedores')
router.register(r'coordenadas', CoordenadasList,'coordenadas' ),
