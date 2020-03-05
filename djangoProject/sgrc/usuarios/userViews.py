from rest_framework import generics

from .userSerializer import UserSerializer

class UserCreate (generics.CreateAPIView):
    #invalidamos configuracion global, para que un usuario pueda crearse sin estar autenticado o tener permisos
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
