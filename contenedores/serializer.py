from rest_framework import serializers
from django.contrib.auth.models import User
from contenedores.models import *
from usuarios.serializers import UserSerializer

class ContenedorSerializer(serializers.ModelSerializer):    
    colaborador = UserSerializer()
    class Meta:
        model = Contenedor
        fields = '__all__'


class ContenedorWriteSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Contenedor
        fields = '__all__'