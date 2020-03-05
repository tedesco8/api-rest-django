from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuarios.models import User, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reputation',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('reputation',)

#admin.site.register(ProfileAdmin)