from django.urls import path, include
from rest_framework import routers
from EvaluateHub.views import *

router = routers.DefaultRouter()
router.register('evaluation-form', EvaluationFormViewSet, basename='evaluation-form')
router.register('students-affairs', StudentsAffairsViewSet, basename='students-affairs')
router.register('security-safety', SecuritySafetyViewSet, basename='security-safety')
router.register('teachers', TeachersViewSet, basename='teachers')
router.register('workers-affairs', WorkersAffairsViewSet, basename='workers-affairs')
router.register('strategic-planning', StrategicPlanningViewSet, basename='strategic-planning')
router.register('administration', AdministrationViewSet, basename='administration')
router.register('training', TrainingViewSet, basename='training')
router.register('nutrition', NutritionViewSet, basename='nutrition')
router.register('cooperative', CooperativeViewSet, basename='cooperative')
router.register('decentralization', DecentralizationViewSet, basename='decentralization')
router.register('production-unit', ProductionUnitViewSet, basename='production-unit')
router.register('environment-population', EnvironmentPopulationViewSet, basename='environment-population')
router.register('laboratories', LaboratoriesViewSet, basename='laboratories')
router.register('quality', QualityViewSet, basename='quality')
urlpatterns = [
    path('', include(router.urls)),
]