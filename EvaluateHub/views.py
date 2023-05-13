from django.db.models import Count, Sum
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet, ModelViewSet
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
        if self.request.method == 'POST':
            return [IsTracker()]
        return [IsManagerOrIsViceOrIsTracker()]


class EvaluationFormInfoViewSet(ReadOnlyModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [IsManagerOrIsViceOrIsTracker]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = ['school_level']
    search_fields = ['school_name', 'school_id', 'school_level']
    serializer_class = EvaluationFormInfoSerializer
    def get_queryset(self):
        if self.request.user.role == 'tracker':
            return EvaluationForm.objects \
                .filter(created_by=self.request.user.id) \
                .select_related('created_by') \
                .all()
        return EvaluationForm.objects \
            .select_related('created_by') \
            .all()

class SecuritySafetyStaticsViewSet(ViewSet):
    def list (self, request, pk=None):
        schools_data = SchoolInfo.objects.get(pk=1)
        security_safety_no_issues = schools_data.total_schools - schools_data.security_safety_issues
        security_safety_no_responses = schools_data.security_safety_issues - schools_data.security_safety_responses
        security_factors = SecurityFactors.objects.aggregate(
            fire_line_valid=Count('fire_line', filter = Q(fire_line=valid)),
            fire_line_invalid=Count('fire_line', filter = Q(fire_line=invalid)),
            tanks_valid=Count('tanks', filter = Q(tanks=valid)),
            tanks_invalid=Count('tanks', filter = Q(tanks=invalid)),
            buckets_valid=Count('buckets', filter = Q(buckets=valid)),
            buckets_invalid=Count('buckets', filter = Q(buckets=invalid)),
            fire_extinguishers_valid=Count('fire_extinguishers', filter = Q(fire_extinguishers=valid)),
            fire_extinguishers_invalid=Count('fire_extinguishers', filter = Q(fire_extinguishers=invalid)),
        )
        security_safety = SecuritySafety.objects.aggregate(
            labs_disciplined=Count('labs', filter = Q(labs=disciplined)),
            labs_undisciplined=Count('labs', filter = Q(labs=undisciplined)),
            cabins_disciplined=Count('cabins', filter = Q(cabins=disciplined)),
            cabins_undisciplined=Count('cabins', filter = Q(cabins=undisciplined)),
            building_disciplined=Count('building', filter = Q(building=disciplined)),
            building_undisciplined=Count('building', filter = Q(building=undisciplined)),
            wall_disciplined=Count('wall', filter = Q(wall=disciplined)),
            wall_undisciplined=Count('wall', filter = Q(wall=undisciplined)),
            external_factors_disciplined=Count('external_factors', filter = Q(external_factors=disciplined)),
            external_factors_undisciplined=Count('external_factors', filter = Q(external_factors=undisciplined)),
        )
        serializer_one = SecurityFactorsStaticsSerializer(security_factors)
        serializer_two = SecuritySafetyStaticsSerializer(security_safety)
        merged_result = {**serializer_one.data, **serializer_two.data}
        data = {
            'system_info': {
                'total_schools': schools_data.total_schools,
                'last_school_added': schools_data.last_school_added,
                'issues': schools_data.security_safety_issues,
                'no_issues': security_safety_no_issues,
                'responses': schools_data.security_safety_responses,
                'no_responses': security_safety_no_responses,
            },
            'security_safety': merged_result,
        }
        return Response(data)

class NutritionStaticsViewSet(ViewSet):
    def list(self, request, pk=None):
        schools_data = SchoolInfo.objects.get(pk=1)
        nutrition_no_issues = schools_data.total_schools - schools_data.nutrition_issues
        nutrition_no_responses = schools_data.nutrition_issues - schools_data.nutrition_responses
        nutrition = Nutrition.objects.aggregate(
            daily_received_exits = Count('daily_received', filter = Q(daily_received=exits)),
            daily_received_noexist = Count('daily_received', filter = Q(daily_received=noexist)),
            daily_served_exits = Count('daily_served', filter = Q(daily_served=exits)),
            daily_served_noexist = Count('daily_served', filter = Q(daily_served=noexist)),
            disciplined_distribution_exits = Count('disciplined_distribution', filter = Q(disciplined_distribution=exits)),
            disciplined_distribution_noexist = Count('disciplined_distribution', filter = Q(disciplined_distribution=noexist)),
            health_certificate_exits = Count('health_certificate', filter = Q(health_certificate=exits)),
            health_certificate_noexist = Count('health_certificate', filter = Q(health_certificate=noexist)),
            not_stored_periods_exits = Count('not_stored_periods', filter = Q(not_stored_periods=exits)),
            not_stored_periods_noexist = Count('not_stored_periods', filter = Q(not_stored_periods=noexist)),
        )
        serializer = NutritionStaticsSerializer(nutrition)
        data = {
            'system_info': {
                'total_schools': schools_data.total_schools,
                'last_school_added': schools_data.last_school_added,
                'issues': schools_data.nutrition_issues,
                'no_issues': nutrition_no_issues,
                'responses': schools_data.nutrition_responses,
                'no_responses': nutrition_no_responses,
            },
            'nutrition': serializer.data,
        }
        return Response(data)

class CooperativeStaticsViewSet(ViewSet):
    def list(self, request, pk=None):
        schools_data = SchoolInfo.objects.get(pk=1)
        cooperative_no_issues = schools_data.total_schools - schools_data.cooperative_issues
        cooperative_no_responses = schools_data.cooperative_issues - schools_data.cooperative_responses
        cooperative = Cooperative.objects.aggregate(
            existing_authorized_items_exits = Count('existing_authorized_items', filter = Q(existing_authorized_items=exits)),
            existing_authorized_items_noexist = Count('existing_authorized_items', filter = Q(existing_authorized_items=noexist)),
            drag_running_exits = Count('drag_running', filter = Q(drag_running=exits)),
            drag_running_noexist = Count('drag_running', filter = Q(drag_running=noexist)),
            drag_profits_exits = Count('drag_profits', filter = Q(drag_profits=exits)),
            drag_profits_noexist = Count('drag_profits', filter = Q(drag_profits=noexist)),)
        serializer = CooperativeStaticsSerializer(cooperative)
        data = {
            'system_info': {
                'total_schools': schools_data.total_schools,
                'last_school_added': schools_data.last_school_added,
                'issues': schools_data.cooperative_issues,
                'no_issues': cooperative_no_issues,
                'responses': schools_data.cooperative_responses,
                'no_responses': cooperative_no_responses,
            },
            'cooperative': serializer.data,
        }
        return Response(data)

class TrainingStaticsViewSet(ViewSet):
    def list (self, request, pk=None):
        schools_data = SchoolInfo.objects.get(pk=1)
        training_no_issues = schools_data.total_schools - schools_data.training_issues
        training_no_responses = schools_data.training_issues - schools_data.training_responses
        training = Training.objects.aggregate(
            teachers_training_exits = Count('teachers_training', filter = Q(teachers_training=exits)),
            teachers_training_noexist = Count('teachers_training', filter = Q(teachers_training=noexist)),
            training_plan_exits = Count('training_plan', filter = Q(training_plan=exits)),
            training_plan_noexist = Count('training_plan', filter = Q(training_plan=noexist)),
            training_plan_activation_exits = Count('training_plan_activation', filter = Q(training_plan_activation=exits)),
            training_plan_activation_noexist = Count('training_plan_activation', filter = Q(training_plan_activation=noexist)),)
        serializer = TrainingStaticsSerializer(training)
        data = {
            'system_info': {
                'total_schools': schools_data.total_schools,
                'last_school_added': schools_data.last_school_added,
                'issues': schools_data.training_issues,
                'no_issues': training_no_issues,
                'responses': schools_data.training_responses,
                'no_responses': training_no_responses,
            },
            'training': serializer.data,
        }
        return Response(data)


class DecentralizationStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        decentralization_no_issues = school_data.total_schools - school_data.decentralization_issues
        decentralization_no_responses = school_data.decentralization_issues - school_data.decentralization_responses
        decentralization = Decentralization.objects.aggregate(
            board_of_trustees_exits = Count('board_of_trustees', filter = Q(board_of_trustees=exits)),
            board_of_trustees_noexist = Count('board_of_trustees', filter = Q(board_of_trustees=noexist)),
            decentralization_committee_exits = Count('decentralization_committee', filter = Q(decentralization_committee=exits)),
            decentralization_committee_noexist = Count('decentralization_committee', filter = Q(decentralization_committee=noexist)),
            settlement_exits = Count('settlement', filter = Q(settlement=exits)),
            settlement_noexist = Count('settlement', filter = Q(settlement=noexist)),
            exchange_exits = Count('exchange', filter = Q(exchange=exits)),
            exchange_noexist = Count('exchange', filter = Q(exchange=noexist)),
            plan_exits = Count('plan', filter = Q(plan=exits)),
            plan_noexist = Count('plan', filter = Q(plan=noexist)),
            append_exits = Count('append', filter = Q(append=exits)),
            append_noexist = Count('append', filter = Q(append=noexist)),)
        serializer = DecentralizationStaticsSerializer(decentralization)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.decentralization_issues,
                'no_issues': decentralization_no_issues,
                'responses': school_data.decentralization_responses,
                'no_responses': decentralization_no_responses,
            },
            'decentralization': serializer.data,
        }
        return Response(data)

class ProductionUnitStaticsViewSet(ViewSet):
    def list(self, request, pk=None):
        school_data = SchoolInfo.objects.get(pk=1)
        production_unit_no_issues = school_data.total_schools - school_data.production_unit_issues
        production_unit_no_responses = school_data.production_unit_issues - school_data.production_unit_responses
        production_unit = ProductionUnit.objects.aggregate(
            profit_distribution_exits = Count('profit_distribution', filter = Q(profit_distribution=exits)),
            profit_distribution_noexist = Count('profit_distribution', filter = Q(profit_distribution=noexist)),
            supply_exits = Count('supply', filter = Q(supply=exits)),
            supply_noexist = Count('supply', filter = Q(supply=noexist)),
            activation_exits = Count('activation', filter = Q(activation=exits)),
            activation_noexist = Count('activation', filter = Q(activation=noexist)),
            certified_exits = Count('certified', filter = Q(certified=exits)),
            certified_noexist = Count('certified', filter = Q(certified=noexist)),)
        serializer = ProductionUnitStaticsSerializer(production_unit)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.production_unit_issues,
                'no_issues': production_unit_no_issues,
                'responses': school_data.production_unit_responses,
                'no_responses': production_unit_no_responses,
            },
            'production_unit': serializer.data,
        }
        return Response(data)

class StrategicPlanningStaticsViewSet(ViewSet):
    def list(self, request, pk=None):
        school_data = SchoolInfo.objects.get(pk=1)
        strategic_planning_no_issues = school_data.total_schools - school_data.strategic_planning_issues
        strategic_planning_no_responses = school_data.strategic_planning_issues - school_data.strategic_planning_responses
        strategic_planning = StrategicPlanning.objects.aggregate(
            obstacles_exits = Count('obstacles', filter = Q(obstacles=exits)),
            obstacles_noexist = Count('obstacles', filter = Q(obstacles=noexist)),
            plan_activation_exits = Count('plan_activation', filter = Q(plan_activation=exits)),
            plan_activation_noexist = Count('plan_activation', filter = Q(plan_activation=noexist)),
            team_building_exits = Count('team_building', filter = Q(team_building=exits)),
            team_building_noexist = Count('team_building', filter = Q(team_building=noexist)),
            plan_exits = Count('plan', filter = Q(plan=exits)),
            plan_noexist = Count('plan', filter = Q(plan=noexist)),
            analysis_exits = Count('analysis', filter = Q(analysis=exits)),
            analysis_noexist = Count('analysis', filter = Q(analysis=noexist)),)
        serializer = StrategicPlanningStaticsSerializer(strategic_planning)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.strategic_planning_issues,
                'no_issues': strategic_planning_no_issues,
                'responses': school_data.strategic_planning_responses,
                'no_responses': strategic_planning_no_responses,
            },
            'strategic_planning': serializer.data,
        }
        return Response(data)

class EnvironmentPopulationStaticsViewSet(ViewSet):
    def list(self, request, pk = None):
        school_data = SchoolInfo.objects.get(pk=1)
        environment_population_no_issues = school_data.total_schools - school_data.environment_population_issues
        environment_population_no_responses = school_data.environment_population_issues - school_data.environment_population_responses
        environment_population = EnvironmentPopulation.objects.aggregate(
            toilets_health_procedures_exits = Count('toilets_health_procedures', filter = Q(toilets_health_procedures=exits)),
            toilets_health_procedures_noexist = Count('toilets_health_procedures', filter = Q(toilets_health_procedures=noexist)),
            health_file_exits = Count('health_file', filter = Q(health_file=exits)),
            health_file_noexist = Count('health_file', filter = Q(health_file=noexist)),
            diagnosis_health_plan_exits = Count('diagnosis_health_plan', filter = Q(diagnosis_health_plan=exits)),
            diagnosis_health_plan_noexist = Count('diagnosis_health_plan', filter = Q(diagnosis_health_plan=noexist)),     
            check_health_plan_exits = Count('check_health_plan', filter = Q(check_health_plan=exits)),
            check_health_plan_noexist = Count('check_health_plan', filter = Q(check_health_plan=noexist)),
            activities_exits = Count('activities', filter = Q(activities=exits)),
            activities_noexist = Count('activities', filter = Q(activities=noexist)),
            labs_health_procedures_exits =  Count('labs_health_procedures', filter = Q(labs_health_procedures=exits)),
            labs_health_procedures_noexist = Count('labs_health_procedures', filter = Q(labs_health_procedures=noexist)),)
        serializer = EnvironmentPopulationStaticsSerializer(environment_population)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.environment_population_issues,
                'no_issues': environment_population_no_issues,
                'responses': school_data.environment_population_responses,
                'no_responses': environment_population_no_responses,
            },
            'environment_population': serializer.data,
        }
        return Response(data)

class AdministrationStaticsViewSet(ViewSet):
    def list(self, request, pk = None):
        school_data = SchoolInfo.objects.get(pk=1)
        administration_no_issues = school_data.total_schools - school_data.administration_issues
        administration_no_responses = school_data.administration_issues - school_data.administration_responses
        administration = Administration.objects.aggregate(
            execution_plan_exits = Count('execution_plan', filter = Q(execution_plan=exits)), 
            execution_plan_noexist = Count('execution_plan', filter = Q(execution_plan=noexist)),
            team_building_exits = Count('team_building', filter = Q(team_building=exits)),
            team_building_noexist = Count('team_building', filter = Q(team_building=noexist)),
            analysis_exits = Count('analysis', filter = Q(analysis=exits)),
            analysis_noexist = Count('analysis', filter = Q(analysis=noexist)),
            activities_activation_exits = Count('activities_activation', filter = Q(activities_activation=exits)),
            activities_activation_noexist = Count('activities_activation', filter = Q(activities_activation=noexist)),
            obstacles_exits = Count('obstacles', filter = Q(obstacles=exits)),
            obstacles_noexist = Count('obstacles', filter = Q(obstacles=noexist)),
            predicted_crisis_exits = Count('predicted_crisis', filter = Q(predicted_crisis=exits)),
            predicted_crisis_noexist = Count('predicted_crisis', filter = Q(predicted_crisis=noexist)),
            communication_system_exits = Count('communication_system', filter = Q(communication_system=exits)),
            communication_system_noexist = Count('communication_system', filter = Q(communication_system=noexist)),
            risks_indicators_exits = Count('risks_indicators', filter = Q(risks_indicators=exits)),
            risks_indicators_noexist = Count('risks_indicators', filter = Q(risks_indicators=noexist)),
            plan_exits = Count('plan', filter = Q(plan=exits)),
            plan_noexist = Count('plan', filter = Q(plan=noexist)),
            training_on_plan_exits = Count('training_on_plan', filter = Q(training_on_plan=exits)),
            training_on_plan_noexist = Count('training_on_plan', filter = Q(training_on_plan=noexist)),)
        serializer = AdministrationStaticsSerializer(administration)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.administration_issues,
                'no_issues': administration_no_issues,
                'responses': school_data.administration_responses,
                'no_responses': administration_no_responses,
            },
            'administration': serializer.data,
        }
        return Response(data)

class LaboratoriesStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        laboratories_no_issues = school_data.total_schools - school_data.laboratories_issues
        laboratories_no_responses = school_data.laboratories_issues - school_data.laboratories_responses
        laboratories = Laboratories.objects.aggregate(
            work_validity_exits = Count('work_validity', filter = Q(work_validity=exits)),
            work_validity_noexist = Count('work_validity', filter = Q(work_validity=noexist)),
            ory_association = Sum('ory_association'),
            networks = Sum('networks'),
            computers = Sum('computers'),
            evaluation = Sum('evaluation'),
            tilo = Sum('tilo'),)
        serializer = LaboratoriesStaticsSerializer(laboratories)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.laboratories_issues,
                'no_issues': laboratories_no_issues,
                'responses': school_data.laboratories_responses,
                'no_responses': laboratories_no_responses,
            },
            'laboratories': serializer.data,
        }
        return Response(data)

class WorkersAffairsStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        workers_affairs_no_issues = school_data.total_schools - school_data.workers_affairs_issues
        workers_affairs_no_responses = school_data.workers_affairs_issues - school_data.workers_affairs_responses
        workers_affairs = WorkersAffairs.objects.aggregate(
            percentage_of_absence_gt_10 = Count('percentage_of_absence', filter = Q(percentage_of_absence__gte=10)),
            percentage_of_absence_gt_20 = Count('percentage_of_absence', filter = Q(percentage_of_absence__gte=20)),
            percentage_of_absence_gt_30 = Count('percentage_of_absence', filter = Q(percentage_of_absence__gte=30)),
            percentage_of_absence_gt_40 = Count('percentage_of_absence', filter = Q(percentage_of_absence__gte=40)),
            percentage_of_absence_gt_50 = Count('percentage_of_absence', filter = Q(percentage_of_absence__gte=50)),)
        serializer = WorkersAffairsStaticsSerializer(workers_affairs)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.workers_affairs_issues,
                'no_issues': workers_affairs_no_issues,
                'responses': school_data.workers_affairs_responses,
                'no_responses': workers_affairs_no_responses,
            },
            'workers_affairs': serializer.data,
        }
        return Response(data)

