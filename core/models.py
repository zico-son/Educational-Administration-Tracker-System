from django.contrib.auth.models import AbstractUser as BaseAbstractUser
from django.db import models
# Models are the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.


class User(BaseAbstractUser):
    system_admin = 'system_admin'
    manager = 'manager'
    vice = 'vice'
    tracker = 'tracker'
    students_affairs_admin = 'students_affairs_admin'
    environment_population_admin = 'environment_population_admin'
    production_unit_admin = 'production_unit_admin'
    laboratories_admin = 'laboratories_admin'
    cooperative_admin = 'cooperative_admin'
    decentralization_admin = 'decentralization_admin'
    workers_affairs_admin = 'workers_affairs_admin'
    security_safety_admin = 'security_safety_admin'
    teachers_admin = 'teachers_admin'
    strategic_planning_admin = 'strategic_planning_admin'
    administration_admin = 'administration_admin'
    quality_admin = 'quality_admin'
    training_admin = 'training_admin'
    nutrition_admin = 'nutrition_admin'

    roles = [
        (system_admin, 'system_admin'),
        (manager, 'manager'),
        (vice, 'vice'),
        (tracker, 'tracker'),
        (students_affairs_admin, 'students_affairs_admin'),
        (environment_population_admin, 'environment_population_admin'),
        (production_unit_admin, 'production_unit_admin'),
        (laboratories_admin, 'laboratories_admin'),
        (cooperative_admin, 'cooperative_admin'),
        (decentralization_admin, 'decentralization_admin'),
        (workers_affairs_admin, 'workers_affairs_admin'),
        (security_safety_admin, 'security_safety_admin'),
        (teachers_admin, 'teachers_admin'),
        (strategic_planning_admin, 'strategic_planning_admin'),
        (administration_admin, 'administration_admin'),
        (quality_admin, 'quality_admin'),
        (training_admin, 'training_admin'),
        (nutrition_admin, 'nutrition_admin'),
    ] 
    role = models.CharField(max_length=255, null=True, blank=True, choices= roles)
    email = models.EmailField(unique=True)