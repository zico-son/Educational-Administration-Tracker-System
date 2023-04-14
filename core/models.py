from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django.db import models
# Models are the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

class User(BaseAbstractUser):
    pass
    # A model that is the base for all users in the system.
    # AbstractUser is a base class that can be used to create custom user models. It contains all the fields and behaviors that are required for a user model, but none of the specific fields and behaviors that are used for a typical user model.
    # The only required field is username, which is used to authenticate the user. Other fields are optional, but recommended.

    # Fields
    # username
    # password
    # last_login
    # is_superuser
    # first_name
    # last_name
    # email
    # is_staff
    # is_active
    # date_joined

    # Methods
    # get_full_name()
    # get_short_name()
    # set_password(raw_password)
    # check_password(raw_password)
    # set_unusable_password()
    # has_usable_password()
    # has_perm(perm, obj=None)
    # has_perms(perm_list, obj=None)
    # has_module_perms(app_label)
    # get_group_permissions(obj=None)
    # get_all_permissions(obj=None)
    # has_perm(perm, obj=None)
    # has_perms(perm_list, obj=None)
    # has_module_perms(app_label)
    # get_group_permissions(obj=None)
    # get_all_permissions(obj=None)
    # is_anonymous()
    # is_authenticated()
    # save(*args, **kwargs)
    # delete(*args, **kwargs)
    # __str__()
    # __repr__()
    # __eq__()
    # __ne__()
    # __hash__()
    # __bool__()
    # __unicode__()
    # __format__()
    # __getattribute__()
    # __setattr__()
    # __delattr__()
    # __lt__()
    # __le__()
    # __gt__()
    # __ge__()
    # __init__()
    # __new__()
    # __reduce__()
    # __reduce_ex__()
    # __setstate__()
    # __sizeof__()
    # __dir__()
    # __class__
    # __dict__
    # __doc__
    # __module__
    # __weakref__

    # Meta
    # abstract = True
    # permissions = None
    # verbose_name = 'user'
    # verbose_name_plural = 'users'
    # db_table = 'auth_user'
    # swappable = 'AUTH_USER