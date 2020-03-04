from django.db import models
from django.contrib.auth.models import AbstractUser
# from cride.core.validators import RegexValidator

from .utils.models import CRideModel


class User(CRideModel, AbstractUser):
    #establecemos el email como campo unico
    email = models.EmailField(
        'email addres',
        unique = True,
        error_messages = {
            'unique': 'Ya exíste un usuario con este email'
        }
    )

    #numero de telefono
    # phone_regex = RegexValidator (
    #     regex = r'\+?1?\d{9,15}$',
    #     message = "El numero de telefono debe contener entre 9 y 15 digitos."
    # )
    phone_number = models.CharField(
        # validators = [phone_regex]
        max_length = 17, 
        blank = True
    )

    #establecemos el correo como identificador principal
    USERNAME_FIELD = 'email'

    #todos los usuarios que se crean tienen que tener al menos estos campos
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    #determinamos que tipo de usuario es, si es admin o client
    is_client = models.BooleanField (
        'client status',
        default = True,
        help_text = (
            'Ayuda a distinguir fácilmente a los usuarios y las consultas.' 
            'Los clientes son el tipo principal de usuario'
        )
    )

    #Nos indica que el usuario a confirmado su correo electronico
    is_verified = models.BooleanField (
        'verified',
        default = True,
        help_text = 'Se establece en verdadero cuando el usuario ha verificado su direccion de correo electrónico'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username