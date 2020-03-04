from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User, Profile

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('users', 'reputation', 'deposit')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('reputation')

admin.site.register(User. CustomUserAdmin)