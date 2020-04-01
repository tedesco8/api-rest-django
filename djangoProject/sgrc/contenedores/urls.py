from contenedores.views import ContenedorViewSet, CoordenadasList
from rest_framework.routers import DefaultRouter
app_name="contenedores"

#Los router generan automaticamente las estructuras de URLs tipicas.
#Si no se especifica el basename, se genera automaticamente en base al queryset de la viewset
router = DefaultRouter()
router.register(r'contenedores', ContenedorViewSet,'contenedores')
router.register(r'coordenadas', CoordenadasList,'coordenadas' ),
