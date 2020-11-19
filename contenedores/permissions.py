from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = "No es el propietario"

    #retorna verdadero si tiene permisos, si no retorna falso
    def has_object_permission(self, request, view, obj):
        #si el metodo que se esta utilizando esta en una lista segura, (GET, OPTION, HEAD), procede
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner