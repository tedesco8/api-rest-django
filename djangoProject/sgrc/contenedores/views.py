from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Contenedor
from .serializer import ContenedorSerializer, ContenedorWriteSerializer

#debugger
import pdb

#ModelViewSet genera todos los los endpoint de CRUD  
class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorWriteSerializer
    # permission_classes = (IsAdminUser,)

    '''
    def get_queryset(self):
        return Contenedor.objects.all()

    def get_serializer_class(self):        
        if self.request.method=='GET':            
            return ContenedorSerializer
        ContenedorSerializer
    '''
