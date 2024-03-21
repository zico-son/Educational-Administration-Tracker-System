from django.urls import path, include
from rest_framework import routers
from PlanHub.views import *


router = routers.DefaultRouter()
router.register('plan', DepartmentPlanViewSet, basename='plan')
router.register('manger-plan', ManagerPlanViewSet, basename='manger-plan')
router.register('post-file', PostFileViewSet, basename='post-file')

urlpatterns = [
    path('', include(router.urls)),
]