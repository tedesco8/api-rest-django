from rest_framework import serializers
from django.contrib.auth.models import User

class ContenedorSerializer(serializers.ModelSerializer):
    #con hiddenfield le decimos que el valor vaya oculto
    owner = serializers.HiddenField(
        #capturamos al usuario loggueado
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Contenedor
        fields = '__all__'