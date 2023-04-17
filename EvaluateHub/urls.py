from django.urls import path, include
from rest_framework import routers
from EvaluateHub.views import *

router = routers.DefaultRouter()
router.register('students-affairs', StudentsAffairsViewSet, basename='students-affairs')

urlpatterns = [
    path('', include(router.urls)),
]