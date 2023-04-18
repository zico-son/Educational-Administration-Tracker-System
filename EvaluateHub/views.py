from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from EvaluateHub.models import *
from EvaluateHub.serializers import *


class StudentsAffairsViewSet(ModelViewSet):
    queryset = StudentsAffairs.objects.all()
    serializer_class = StudentsAffairsSerializer

class EvaluationFormViewSet(ModelViewSet):

    def get_queryset(self):
        return EvaluationForm.objects.all()
    
    def get_serializer_class(self):
        return EvaluationFormSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}