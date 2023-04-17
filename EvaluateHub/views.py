from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from EvaluateHub.models import *
from EvaluateHub.serializers import *


class StudentsAffairsViewSet(ModelViewSet):
    queryset = StudentsAffairs.objects.all()
    serializer_class = StudentsAffairsSerializer