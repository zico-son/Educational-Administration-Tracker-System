from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from EvaluateHub.models import *
from EvaluateHub.serializers import *
from EvaluateHub.admin_serializers import *
from EvaluateHub.custom_view_set import NoPostViewSet, NoUpdateViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from EvaluateHub.permissions import *
from EvaluateHub.pagination import CustomPagination 

class StudentsAffairsViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('students_affairs__first_class') \
        .select_related('students_affairs__issue') \
        .select_related('students_affairs__response') \
        .all()
    serializer_class = AdminStudentsEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsStudentAffairsAdmin()]
        return [IsManagerOrIsViceOrIsStudentAffairsAdmin()]

class WorkersAffairsViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('workers_affairs__issue') \
        .select_related('workers_affairs__response') \
        .all()
    serializer_class = AdminWorkersEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsWorkersAffairsAdmin()]
        return [IsManagerOrIsViceOrIsWorkersAffairsAdmin()]

class SecuritySafetyViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('security_safety__security_factors') \
        .select_related('security_safety__issue') \
        .select_related('security_safety__response') \
        .all()
    serializer_class = AdminSecuritySafetyEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsSecuritySafetyAdmin()]
        return [IsManagerOrIsViceOrIsSecuritySafetyAdmin()]

class TeachersViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('teachers__material_one') \
        .select_related('teachers__issue') \
        .select_related('teachers__response') \
        .all()
    serializer_class = AdminTeachersEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsTeachersAdmin()]
        return [IsManagerOrIsViceOrIsTeachersAdmin()]

class StrategicPlanningViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('strategic_planning__issue') \
        .select_related('strategic_planning__response') \
        .all()
    serializer_class = AdminStrategicPlanningEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsStrategicPlanningAdmin()]
        return [IsManagerOrIsViceOrIsStrategicPlanningAdmin()]

class AdministrationViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('administration__issue') \
        .select_related('administration__response') \
        .all()
    serializer_class = AdminAdministrationEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsAdministrationAdmin()]
        return [IsManagerOrIsViceOrIsAdministrationAdmin()]

class TrainingViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('training__issue') \
        .select_related('training__response') \
        .all()
    serializer_class = AdminTrainingEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsTrainingAdmin()]
        return [IsManagerOrIsViceOrIsTrainingAdmin()]

class NutritionViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('nutrition__issue') \
        .select_related('nutrition__response') \
        .all()
    serializer_class = AdminNutritionEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsNutritionAdmin()]
        return [IsManagerOrIsViceOrIsNutritionAdmin()]

class CooperativeViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('cooperative__issue') \
        .select_related('cooperative__response') \
        .all()
    serializer_class = AdminCooperativeEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsCooperativeAdmin()]
        return [IsManagerOrIsViceOrIsCooperativeAdmin()]

class LaboratoriesViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('laboratories__issue') \
        .select_related('laboratories__response') \
        .all()
    serializer_class = AdminLaboratoriesEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsLaboratoriesAdmin()]
        return [IsManagerOrIsViceOrIsLaboratoriesAdmin()]

class DecentralizationViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('decentralization__issue') \
        .select_related('decentralization__response') \
        .all()
    serializer_class = AdminDecentralizationEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsDecentralizationAdmin()]
        return [IsManagerOrIsViceOrIsDecentralizationAdmin()]

class ProductionUnitViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('production_unit__issue') \
        .select_related('production_unit__response') \
        .all()
    serializer_class = AdminProductionUnitEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsProductionUnitAdmin()]
        return [IsManagerOrIsViceOrIsProductionUnitAdmin()]

class QualityViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('quality__issue') \
        .select_related('quality__response') \
        .all()
    serializer_class = AdminQualityEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsQualityAdmin()]
        return [IsManagerOrIsViceOrIsQualityAdmin()]

class EnvironmentPopulationViewSet(NoPostViewSet):
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['id', 'school_name', 'school_id', 'school_level']
    queryset = EvaluationForm.objects \
        .select_related('environment_population__issue') \
        .select_related('environment_population__response') \
        .all()
    serializer_class = AdminEnvironmentPopulationEvaluationFormSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsEnvironmentPopulationAdmin()]
        return [IsManagerOrIsViceOrIsEnvironmentPopulationAdmin()]

class EvaluationFormViewSet(NoUpdateViewSet):

    def get_queryset(self):
        return EvaluationForm.objects \
        .select_related('students_affairs__first_class') \
        .select_related('security_safety__security_factors') \
        .select_related('teachers__material_one') \
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
    
    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return [IsTracker()]
        return [IsManagerOrIsViceOrIsTracker()]