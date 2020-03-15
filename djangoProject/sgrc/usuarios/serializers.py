from rest_framework import serializers
from django.contrib.auth.models import User,Group
from rest_framework.authtoken.models import Token
from usuarios.models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    city = CitySerializer(many = False)
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many = False)
    groups = GroupSerializer(many = True)
    class Meta:
        model = User
        fields = '__all__'

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'    
    