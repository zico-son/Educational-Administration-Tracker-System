from django.urls import path, include
from rest_framework import routers
from EvaluateHub.views import *

router = routers.DefaultRouter()
router.register('evaluation-form', EvaluationFormViewSet, basename='evaluation-form')
router.register('form-info', EvaluationFormInfoViewSet, basename='form-info')
router.register('students-affairs', StudentsAffairsViewSet, basename='students-affairs')
router.register('teachers', TeachersViewSet, basename='teachers')
router.register('workers-affairs', WorkersAffairsViewSet, basename='workers-affairs')
router.register('workers-affairs-statics', WorkersAffairsStaticsViewSet, basename='workers-affairs-statics')
router.register('laboratories', LaboratoriesViewSet, basename='laboratories')
router.register('laboratories-statics', LaboratoriesStaticsViewSet, basename='laboratories-statics')
router.register('quality', QualityViewSet, basename='quality')
router.register('security-safety', SecuritySafetyViewSet, basename='security-safety')
router.register('security-safety-statics', SecuritySafetyStaticsViewSet, basename='security-safety-statics')
router.register('nutrition', NutritionViewSet, basename='nutrition')
router.register('nutrition-statics', NutritionStaticsViewSet, basename='nutrition-statics')
router.register('cooperative', CooperativeViewSet, basename='cooperative')
router.register('cooperative-statics', CooperativeStaticsViewSet, basename='cooperative-statics')
router.register('strategic-planning', StrategicPlanningViewSet, basename='strategic-planning')
router.register('strategic-planning-statics', StrategicPlanningStaticsViewSet, basename='strategic-planning-statics')
router.register('administration', AdministrationViewSet, basename='administration')
router.register('administration-statics', AdministrationStaticsViewSet, basename='administration-statics')
router.register('training', TrainingViewSet, basename='training')
router.register('training-statics', TrainingStaticsViewSet, basename='training-statics')
router.register('decentralization', DecentralizationViewSet, basename='decentralization')
router.register('decentralization-statics', DecentralizationStaticsViewSet, basename='decentralization-statics')
router.register('production-unit', ProductionUnitViewSet, basename='production-unit')
router.register('production-unit-statics', ProductionUnitStaticsViewSet, basename='production-unit-statics')
router.register('environment-population', EnvironmentPopulationViewSet, basename='environment-population')
router.register('environment-population-statics', EnvironmentPopulationStaticsViewSet, basename='environment-population-statics')
urlpatterns = [
    path('', include(router.urls)),
]