from rest_framework.permissions import BasePermission
from EvaluateHub.utils import permission_exception_handler

class IsStudentAffairsAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'students_affairs_admin')

class IsWorkersAffairsAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'workers_affairs_admin')

class IsSecuritySafetyAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'security_safety_admin')

class IsTeachersAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'teachers_admin') 

class IsStrategicPlanningAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'strategic_planning_admin')

class IsAdministrationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'administration_admin') 

class IsTrainingAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'training_admin')

class IsNutritionAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'nutrition_admin')

class IsCooperativeAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'cooperative_admin') 

class IsDecentralizationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'decentralization_admin') 

class IsProductionUnitAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'production_unit_admin') 

class IsEnvironmentPopulationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'environment_population_admin') 

class IsLaboratoriesAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'laboratories_admin') 

class IsQualityAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'quality_admin') 

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') 

class IsVice(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'vice') 

class IsTracker(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'tracker') 

class IsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'system_admin') 


class IsManagerOrIsViceOrIsStudentAffairsAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'students_affairs_admin')

class IsManagerOrIsViceOrIsWorkersAffairsAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'workers_affairs_admin')

class IsManagerOrIsViceOrIsSecuritySafetyAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'security_safety_admin')

class IsManagerOrIsViceOrIsTeachersAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'teachers_admin')

class IsManagerOrIsViceOrIsStrategicPlanningAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'strategic_planning_admin')

class IsManagerOrIsViceOrIsAdministrationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'administration_admin')

class IsManagerOrIsViceOrIsTrainingAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'training_admin')

class IsManagerOrIsViceOrIsNutritionAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'nutrition_admin')

class IsManagerOrIsViceOrIsCooperativeAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'cooperative_admin')

class IsManagerOrIsViceOrIsDecentralizationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'decentralization_admin')

class IsManagerOrIsViceOrIsProductionUnitAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'production_unit_admin') or permission_exception_handler(request, 'vice')

class IsManagerOrIsViceOrIsEnvironmentPopulationAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'environment_population_admin') or permission_exception_handler(request, 'vice')

class IsManagerOrIsViceOrIsLaboratoriesAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'laboratories_admin') or permission_exception_handler(request, 'vice')

class IsManagerOrIsViceOrIsQualityAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'quality_admin') or permission_exception_handler(request, 'vice')

class IsManagerOrIsViceOrIsSystemAdmin(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'system_admin') or permission_exception_handler(request, 'vice')

class IsManagerOrIsViceOrIsTracker(BasePermission):
    def has_permission(self, request, view):
        return permission_exception_handler(request, 'manager') or permission_exception_handler(request, 'vice') or permission_exception_handler(request, 'tracker')