from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuarios.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','reputation',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('reputation',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)    

#admin.site.register(CityAdmin)