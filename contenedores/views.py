from rest_framework import viewsets,status
from rest_framework.permissions import IsAdminUser

from .models import Contenedor
from .serializer import ContenedorSerializer, ContenedorWriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


#debugger
import pdb

#ModelViewSet genera todos los los endpoint de CRUD
class CoordenadasList(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorWriteSerializer

    @action(detail=False,methods=['GET',])
    def activos(self,request):
        activos_str = request.query_params.get('activos')        
        activos = True if activos_str=='true' else False

        try:
            queryset = Contenedor.objects.filter(activo=activos)
            contenedor_srlzr = ContenedorWriteSerializer(queryset,many=True)
            return Response(
                contenedor_srlzr.data
                )    
        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    @action(detail=True,methods=['GET',])
    def propios(self,request,pk = None):
        try:
            queryset = Contenedor.objects.filter(colaborador=pk)
            contenedor_srlzr = ContenedorWriteSerializer(queryset,many=True)
            return Response(
                contenedor_srlzr.data
                )    
        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

#ModelViewSet genera todos los los endpoint de CRUD  
class ContenedorViewSet(viewsets.ModelViewSet):
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorWriteSerializer

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