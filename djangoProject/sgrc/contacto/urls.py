from contacto.views import sendemailViewSet
from rest_framework.routers import DefaultRouter

import pdb

app_name="contacto"

router = DefaultRouter()

router.register(r'contacto', sendemailViewSet, 'contacto')