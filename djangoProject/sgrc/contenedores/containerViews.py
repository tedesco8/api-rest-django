from rest_framework import viewsets

from .models import Contenedor
from .containerSerializer import ContenedorSerializer
from .permissions import IsOwner

class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer
    permission_classes = [IsOwner]