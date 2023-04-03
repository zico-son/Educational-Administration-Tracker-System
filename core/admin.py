from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Registering models with the admin site for testing purposes

class UserAdmin (BaseUserAdmin):
    pass
# UserAdmin is a class that is used to customize the admin interface for the User model. It is a subclass of django.contrib.auth.admin.UserAdmin.