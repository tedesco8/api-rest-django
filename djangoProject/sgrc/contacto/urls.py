from contacto.views import sendemailViewSet
from rest_framework.routers import DefaultRouter

app_name="contacto"

router = DefaultRouter()
router.register(r'email', sendemailViewSet, 'email')