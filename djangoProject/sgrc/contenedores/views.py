from rest_framework import viewsets

from .models import Contenedor
from .serializer import ContenedorSerializer, ContenedorWriteSerializer
from .permissions import IsOwner
import pdb

class ContenedorViewSet(viewsets.ModelViewSet):
    queryset=Contenedor.objects.all()
    serializer_class=ContenedorWriteSerializer
    '''
    def get_queryset(self):
        return Contenedor.objects.all()

    def get_serializer_class(self):        
        if self.request.method=='GET':            
            return ContenedorSerializer
        ContenedorSerializer
    '''
