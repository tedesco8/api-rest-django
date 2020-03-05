from django.db import models
from django.contrib.auth.models import User

#from ..utils.models import CRideModel


class City(models.Model):
    name = models.CharField (
        max_length = 500,
        blank = True,
        null = True
    )
    description = models.CharField (
        max_length = 500,
        blank = True,
        null = True
    )    
    lat = models.FloatField (
        default = 0,
        blank=True,
        null=True
    )
    lng = models.FloatField (
        default = 0,
        blank=True,
        null=True
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # picture = models.ImageField (
    #     'profile picture',
    #     upload_to = 'users/pictures/',
    #     blank = True,
    #     null = True
    # )

    biography = models.CharField (
        max_length = 500,
        blank = True,
        null = True
    )    

    dni = models.CharField (
        max_length = 500,
        blank = True,
        null = True
    )

    phone = models.CharField (
        max_length = 500,
        blank = True,
        null = True
    )  

    reputation = models.FloatField (
        default = 0,
        help_text = 'Reputació del usuario en base a depositos efectuados'
    )

    address = models.CharField (
        max_length = 500,
        blank = True,
        null=True
    )

    city = models.ForeignKey(City,null=True,blank=True, on_delete=models.SET_NULL,)


    created = models.DateTimeField(
        'created at',
        auto_now_add = True,
        help_text = 'Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now = True,
        help_text = 'Date time on which the object was last created.'
    )


    #da error
    def __str__ (self):
        return str (self.user)