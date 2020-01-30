# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Producto, Categoria, SubCategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer

#-----------------------VISTAS-----------------------------
# class ProductoList(APIView):
#     def get(self, req):
#         prod = Producto.objects.all()[:20]
#         data = ProductoSerializer(prod, many = True).data
#         return Response(data)

# class ProductoDetalle(APIView):
#     def get(self, req, pk):
#         prod = get_object_or_404(Producto, pk=pk)
#         data = ProductoSerializer(prod).data
#         return Response(data)



#------------------VISTAS GENERICAS-------------------------
#Productos
class ProductoList(generics.ListCreateAPIView):
    #devuelve una lista de entindades o las crea
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
 
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    #recupera los datos de una entidad o la elimina
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoSave(generics.CreateAPIView):
    serializer_class = ProductoSerializer

#Categorias
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaSave(generics.CreateAPIView):
    #permite crear entidades pero no las lista
    serializer_class = CategoriaSerializer

#Subcategorias
class SubCategoriaSave(generics.CreateAPIView):
    #permite crear entidades pero no las lista
    serializer_class = SubCategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer