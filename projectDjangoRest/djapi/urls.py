from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-puro/', include('dj_puro.urls')),
    path('api/', include('api.urls'))
]
