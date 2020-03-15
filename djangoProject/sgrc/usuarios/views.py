from rest_framework import viewsets


from usuarios.serializers import *
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

import pdb

class CityViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        no_paginate = self.request.query_params.get('no_paginate', None)

        if no_paginate:
            self.pagination_class = None
        return City.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CitySerializer
        else:
            return CityWriteSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    
    def get_queryset(self):
        no_paginate = self.request.query_params.get('no_paginate', None)

        if no_paginate:
            self.pagination_class = None
        return Profile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProfileSerializer
        else:
            return ProfileWriteSerializer



class UserViewSet (viewsets.ModelViewSet):    
    #serializer_class = UserSerializer
    
    #http://localhost:8000/api/usuarios/users/?search=gmail&roles=colaborador&no_paginate=1
    def get_queryset(self):
        queryset= User.objects.all()

        roles = self.request.query_params.get('roles', None)
        
        no_paginate = self.request.query_params.get('no_paginate', None)

        search = self.request.query_params.get('search', None)

        if no_paginate:
            self.pagination_class = None
        
        if roles:
            roles_array = roles.split(',')            
            queryset = queryset.filter(groups__name__in=roles_array).distinct()

        if search:
            queryset = queryset.filter(
                #Q object para hacer clausulas OR en sentencia sql A or B or C
                Q(username__icontains = search)|
                Q(email__icontains = search)|
                Q(first_name__icontains = search)|
                Q(last_name__icontains = search)
                )

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        else:
            return UserWriteSerializer

    def update(self, request, *args, **kwargs):
        profile_data = request.data.pop('profile')       

        
        response = super().update(request,*args,**kwargs)
        user = User.objects.get(
            id = response.data.get('id')
        )
        user.set_password(
            request.data.get('password','')
        )
        user.save()       
        
        profile_data.pop('city')        

        city=City.objects.all().first()
        profile_data['city'] = city.id

        profile = Profile.objects.get(
            id = profile_data.get('id')
        )

        profile_srlzr = ProfileWriteSerializer(
            profile,data = profile_data
        )

        profile_srlzr.is_valid(
            raise_exception = True
        )
        profile_srlzr.save()

        return response


    def create(self, request, *args, **kwargs):
        profile_data = request.data.pop('profile')       

        response = super().create(request,*args,**kwargs)
        user = User.objects.get(
            id = response.data.get('id')
        )
        user.set_password(
            request.data.get('password','')
        )
        user.save()        

        city = City.objects.all().first()
        profile_data['city'] = city.id
        profile_data['user'] = user.id

        profile_srlzr = ProfileWriteSerializer(
            data = profile_data
        )

        profile_srlzr.is_valid(
            raise_exception = True
        )
        profile_srlzr.save()

        return response
