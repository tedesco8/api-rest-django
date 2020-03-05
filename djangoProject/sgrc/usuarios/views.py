from rest_framework import viewsets


from usuarios.serializers import UserSerializer
from django.contrib.auth.models import User

class UserViewSet (viewsets.ModelViewSet):    
    serializer_class = UserSerializer
    queryset = User.objects.all()
