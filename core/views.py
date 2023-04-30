from django.shortcuts import render

from django.http import JsonResponse

def roles_view(request):
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
    roles_dict = dict(roles)
    return JsonResponse(roles_dict)
