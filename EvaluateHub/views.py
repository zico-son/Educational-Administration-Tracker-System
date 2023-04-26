from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from EvaluateHub.models import *
from EvaluateHub.serializers import *
from EvaluateHub.admin_serializers import *
from EvaluateHub.custom_view_set import NoPostViewSet

class StudentsAffairsViewSet(NoPostViewSet):
    queryset = EvaluationForm.objects.all()
    serializer_class = AdminEvaluationFormSerializer

class EvaluationFormViewSet(ModelViewSet):

    def get_queryset(self):
        return EvaluationForm.objects \
        .select_related('students_affairs__first_class') \
        .select_related('security_safety__security_factors') \
        .select_related('teachers__material_one') \
        .select_related('workers_affairs') \
        .select_related('strategic_planning') \
        .select_related('administration') \
        .select_related('training') \
        .select_related('nutrition') \
        .select_related('cooperative') \
        .select_related('laboratories') \
        .select_related('decentralization') \
        .select_related('production_unit') \
        .select_related('environment_population') \
        .select_related('quality') \
        .select_related('students_affairs__issue') \
        .select_related('security_safety__issue') \
        .select_related('teachers__issue') \
        .select_related('workers_affairs__issue') \
        .select_related('strategic_planning__issue') \
        .select_related('administration__issue') \
        .select_related('training__issue') \
        .select_related('nutrition__issue') \
        .select_related('cooperative__issue') \
        .select_related('laboratories__issue') \
        .select_related('decentralization__issue') \
        .select_related('production_unit__issue') \
        .select_related('environment_population__issue') \
        .select_related('quality__issue') \
        .select_related('students_affairs__response') \
        .select_related('security_safety__response') \
        .select_related('teachers__response') \
        .select_related('workers_affairs__response') \
        .select_related('strategic_planning__response') \
        .select_related('administration__response') \
        .select_related('training__response') \
        .select_related('nutrition__response') \
        .select_related('cooperative__response') \
        .select_related('laboratories__response') \
        .select_related('decentralization__response') \
        .select_related('production_unit__response') \
        .select_related('environment_population__response') \
        .select_related('quality__response') \
        .select_related('students_affairs__response') \
        .all()
    
    def get_serializer_class(self):
        return EvaluationFormSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}