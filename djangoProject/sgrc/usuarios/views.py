from rest_framework import viewsets


from usuarios.serializers import UserSerializer
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response

import pdb

class UserViewSet (viewsets.ModelViewSet):    
    serializer_class = UserSerializer

    #http://localhost:8000/api/usuarios/users/?search=gmail&roles=colaborador&no_paginate=1
    def get_queryset(self):
        queryset= User.objects.all()

        roles = self.request.query_params.get('roles',None)
        
        no_paginate = self.request.query_params.get('no_paginate',None)

        search = self.request.query_params.get('search',None)

        if no_paginate:
            self.pagination_class=None
        
        if roles:
            roles_array = roles.split(',')            
            queryset = queryset.filter(groups__name__in=roles_array).distinct()

        if search:
            queryset = queryset.filter(
                #Q object para hacer clausulas OR en sentencia sql A or B or C
                Q(username__icontains=search)|
                Q(email__icontains=search)|
                Q(first_name__icontains=search)|
                Q(last_name__icontains=search)
                )

        return queryset

    #TODO usar super() de python 3.x
    def create(self, request, *args, **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        user = User.objects.get(id=serializer.data.get('id'))
        user.set_password(request.data.get('password',''))
        user.save()
        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)