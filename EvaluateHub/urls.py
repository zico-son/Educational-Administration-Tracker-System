from django.urls import path, include
from rest_framework import routers
from EvaluateHub.views import *

router = routers.DefaultRouter()
router.register('students-affairs', StudentsAffairsViewSet, basename='students-affairs')
router.register('evaluation-form', EvaluationFormViewSet, basename='evaluation-form')
urlpatterns = [
    path('', include(router.urls)),
]