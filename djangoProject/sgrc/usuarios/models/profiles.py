from django.db import models

from ..utils.models import CRideModel

class Profile(CRideModel):
    users = models.OneToOneField (
        'users.User', 
        on_delete = models.CASCADE
    )

    # picture = models.ImageField (
    #     'profile picture',
    #     upload_to = 'users/pictures/',
    #     blank = True,
    #     null = True
    # )

    biography = models.TextField (
        max_length = 500,
        blank = True
    )

    deposit = models.PositiveIntegerField (
        default = 0
    )

    reputation = models.FloatField (
        default = 0,
        help_text = 'Reputació del usuario en base a depositos efectuados'
    )
    #da error
    def __str__ (self):
        return str (self.user)