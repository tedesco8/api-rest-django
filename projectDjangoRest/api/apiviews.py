# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import generics

# otra manera de agregar subcategorias
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .permissions import IsOwner

from .models import Producto, Categoria, SubCategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubCategoriaSerializer, UserSerializer

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
#Use genéricos.* Cuando solo desee permitir algunas operaciones en un modelo

#----------------------------------Productos--------------------------------------
class ProductoList(generics.ListCreateAPIView):
    #devuelve una lista de entindades o las crea
    permission_classes = ()
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
 
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    permission_classes = ()
    #recupera los datos de una entidad o la elimina
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoSave(generics.CreateAPIView):
    permission_classes = ()
    #permite crear entidades pero no las lista
    serializer_class = ProductoSerializer

#----------------------------------Categorias---------------------------------------
class CategoriaList(generics.ListCreateAPIView):
    #devuelve una lista de entindades o las crea
    permission_classes = ()
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    permission_classes = ()
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaSave(generics.CreateAPIView):
    permission_classes = [IsOwner]
    #permite crear entidades pero no las lista
    serializer_class = CategoriaSerializer

#---------------------------------Subcategorias-------------------------------------
# class SubCategoriaList(generics.ListCreateAPIView):
#     #devuelve una lista de entindades o las crea
#     queryset = SubCategoria.objects.all()
#     serializer_class = SubCategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
    permission_classes = ()
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset
    serializer_class = SubCategoriaSerializer

#----------------------------------Usuarios------------------------------
class UserCreate (generics.CreateAPIView):
    #invalidamos configuracion global, para que un usuario pueda crearse sin estar autenticado o tener permisos
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

#----------------------------------APIVIEW-------------------------------------------
#Usa APIView cuando quieras personalizar completamente el comportamiento

#vamos a sobrescribir el metodo post, tomando en cuenta el valor de la categoria
class SubCategoriaSave(APIView):
    permission_classes = ()
    def post(self, request, cat_pk):
        descripcion = request.data.get("descripcion")
        data = {
            "categoria": cat_pk,
            "descripcion": descripcion
        }
        serializer = SubCategoriaSerializer(data = data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    #Deshabilitamos la autentication para realizar esta accion
    permission_classes = ()
    def post(self, request):

        #capturamos el usuario y la contraseña
        username = request.data.get("username")
        password = request.data.get("password")

        #validamos con la base
        user = authenticate(username = username, password = password)

        if user:
            #si el usuario existe, le devolvemos un token
            return Response(
                {
                    "token": user.auth_token.key
                },
                status=status.HTTP_200_OK
            )
        else:
            #si el usuario no existe, enviamos un bad request
            return Response(
                {
                    "error": "Credenciales incorrectas"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

#--------------------------------------VIEWSET---------------------------
#Use viewsets.ModelViewSet cuando va a permitir todas o la mayoría de las operaciones CRUD en un modelo.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsOwner]

        