from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Registering models with the admin site for testing purposes

class UserAdmin (BaseUserAdmin):
    pass