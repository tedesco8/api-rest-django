from rest_framework import viewsets,status
from rest_framework.permissions import IsAdminUser

from .models import Contenedor
from .serializer import ContenedorSerializer, ContenedorWriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


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

    @action(detail=True,methods=['PUT',])
    def activate(self,request,pk = None):
        try:
            contenedor = Contenedor.objects.get(id=pk)
            contenedor.activo = True
            contenedor.save()
            contenedor_srlzr = ContenedorSerializer(contenedor)
            return Response(
                contenedor_srlzr.data
                )
        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    @action(detail = True, methods = ['PUT',])
    def deactivate(self, request, pk = None):
        try:
            contenedor = Contenedor.objects.get(id=pk)
            contenedor.activo = False
            contenedor.save()
            contenedor_srlzr = ContenedorSerializer(contenedor)
            return Response(
                contenedor_srlzr.data
                )
        except Exception as e:
            return Response(
                str(e),
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
                )