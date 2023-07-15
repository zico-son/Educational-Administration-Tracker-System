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
    search_fields = ['school_name']
    queryset = EvaluationForm.objects \
        .select_related('students_affairs__first_class') \
        .select_related('students_affairs__second_class') \
        .select_related('students_affairs__third_class') \
        .select_related('students_affairs__fourth_class') \
        .select_related('students_affairs__fifth_class') \
        .select_related('students_affairs__sixth_class') \
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
    queryset = EvaluationForm.objects \
        .select_related('teachers__material_one') \
        .select_related('teachers__material_two') \
        .select_related('teachers__material_three') \
        .select_related('teachers__material_four') \
        .select_related('teachers__material_five') \
        .select_related('teachers__material_six') \
        .select_related('teachers__material_seven') \
        .select_related('teachers__material_eight') \
        .select_related('teachers__material_nine') \
        .select_related('teachers__material_ten') \
        .select_related('teachers__material_eleven') \
        .select_related('teachers__material_twelve') \
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
    search_fields = ['school_name']
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
        .select_related('students_affairs__second_class') \
        .select_related('students_affairs__third_class') \
        .select_related('students_affairs__fourth_class') \
        .select_related('students_affairs__fifth_class') \
        .select_related('students_affairs__sixth_class') \
        .select_related('security_safety__security_factors') \
        .select_related('teachers__material_one') \
        .select_related('teachers__material_two') \
        .select_related('teachers__material_three') \
        .select_related('teachers__material_four') \
        .select_related('teachers__material_five') \
        .select_related('teachers__material_six') \
        .select_related('teachers__material_seven') \
        .select_related('teachers__material_eight') \
        .select_related('teachers__material_nine') \
        .select_related('teachers__material_ten') \
        .select_related('teachers__material_eleven') \
        .select_related('teachers__material_twelve') \
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
        if self.request.method == 'GET':
            return EvaluationFormViewSerializer
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
    search_fields = ['school_name']
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


class StudentsAffairsStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        students_affairs_no_issues = school_data.total_schools - school_data.students_affairs_issues
        students_affairs_no_responses = school_data.students_affairs_issues - school_data.students_affairs_responses
        students_affairs = ClassRecord.objects.aggregate(
            percentage_of_absence_primary = Sum('absent', filter= Q(level = 'primary')),
            percentage_of_absence_intermediate = Sum('absent', filter= Q(level = 'intermediate')),
            percentage_of_absence_secondary = Sum('absent', filter= Q(level = 'secondary')),
            percentage_of_registered_primary = Sum('registered', filter= Q(level = 'primary')),
            percentage_of_registered_intermediate = Sum('registered', filter= Q(level = 'intermediate')),
            percentage_of_registered_secondary = Sum('registered', filter= Q(level = 'secondary')))
        if students_affairs['percentage_of_absence_primary'] is not None:
            students_affairs['percentage_of_absence_primary'] = int(students_affairs['percentage_of_absence_primary'] / students_affairs['percentage_of_registered_primary'] * 100)
        if students_affairs['percentage_of_absence_intermediate'] is not None:
            students_affairs['percentage_of_absence_intermediate'] = int (students_affairs['percentage_of_absence_intermediate'] / students_affairs['percentage_of_registered_intermediate'] * 100)
        if students_affairs['percentage_of_absence_secondary'] is not None:    
            students_affairs['percentage_of_absence_secondary'] = int (students_affairs['percentage_of_absence_secondary'] / students_affairs['percentage_of_registered_secondary'] * 100)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.students_affairs_issues,
                'no_issues': students_affairs_no_issues,
                'responses': school_data.students_affairs_responses,
                'no_responses': students_affairs_no_responses,
            },
            'students_affairs': 
                {
                    'percentage_of_absence_primary': students_affairs['percentage_of_absence_primary'],
                    'percentage_of_absence_intermediate': students_affairs['percentage_of_absence_intermediate'],
                    'percentage_of_absence_secondary': students_affairs['percentage_of_absence_secondary'],
                }
        }
        return Response(data)

class QualityStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        quality_no_issues = school_data.total_schools - school_data.quality_issues
        quality_no_responses = school_data.quality_issues - school_data.quality_responses

        quality_with_issues = QualityIssue.objects.only('id').all()
        print (quality_with_issues)
        quality_queryset = Quality.objects.exclude(issue__in=quality_with_issues)
        print (quality_queryset)
        queryset = EvaluationForm.objects.filter(quality__in=quality_queryset)
        print (queryset)

        serializer = SchoolStaticsSerializer(queryset, many=True)
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.quality_issues,
                'no_issues': quality_no_issues,
                'responses': school_data.quality_responses,
                'no_responses': quality_no_responses,
            },
            'quality': serializer.data,
        }
        return Response(data)

class TeachersStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        school_data = SchoolInfo.objects.get(pk=1)
        teachers_no_issues = school_data.total_schools - school_data.teachers_issues
        teachers_no_responses = school_data.teachers_issues - school_data.teachers_responses
        data = {
            'system_info': {
                'total_schools': school_data.total_schools,
                'last_school_added': school_data.last_school_added,
                'issues': school_data.teachers_issues,
                'no_issues': teachers_no_issues,
                'responses': school_data.teachers_responses,
                'no_responses': teachers_no_responses,}
        }
        return Response(data)
    

class ManagerStaticsViewSet(ViewSet):
    def list (self ,request, pk =None):
        # Schools
        schools_with_issues = EvaluationForm.objects.filter(issues=True)
        schools_without_issues = EvaluationForm.objects.filter(issues=False)
        schools_with_issues = SchoolStaticsSerializer(schools_with_issues, many=True)
        schools_without_issues = SchoolStaticsSerializer(schools_without_issues, many=True)
        # Nutrition
        no_daily_received = Nutrition.objects.filter(daily_received=noexist)
        no_health_certificate = Nutrition.objects.filter(health_certificate=noexist)
        not_stored_periods = Nutrition.objects.filter(not_stored_periods=noexist)
        # Training
        no_training_plan = Training.objects.filter(training_plan=noexist) 
        no_teachers_training = Training.objects.filter(teachers_training=noexist) 
        # SecurityFactors
        no_fire_line = SecurityFactors.objects.filter(fire_line=invalid)
        no_fire_line = SecuritySafety.objects.filter(security_factors__in=no_fire_line)
        no_tanks = SecurityFactors.objects.filter(tanks=invalid)
        no_tanks = SecuritySafety.objects.filter(security_factors__in=no_tanks)
        # SecuritySafety
        no_wall = SecuritySafety.objects.filter(wall=undisciplined)
        # Administration
        no_analysis = Administration.objects.filter(analysis=noexist)
        no_risks_indicators = Administration.objects.filter(risks_indicators=noexist)
        # StudentsAffairs
        no_transferred_files = StudentsAffairs.objects.filter(transferred_files=undisciplined)
        # EnvironmentPopulation
        no_labs_health_procedures = EnvironmentPopulation.objects.filter(labs_health_procedures=noexist)
        no_diagnosis_health_plan = EnvironmentPopulation.objects.filter(diagnosis_health_plan=noexist)
        no_toilets_health_procedures = EnvironmentPopulation.objects.filter(toilets_health_procedures=noexist)
        # Teachers

        no_daily_received = EvaluationForm.objects.filter(nutrition__in=no_daily_received)
        no_health_certificate = EvaluationForm.objects.filter(nutrition__in=no_health_certificate)
        not_stored_periods = EvaluationForm.objects.filter(nutrition__in=not_stored_periods)
        no_training_plan = EvaluationForm.objects.filter(training__in=no_training_plan)
        no_teachers_training = EvaluationForm.objects.filter(training__in=no_teachers_training)
        no_fire_line = EvaluationForm.objects.filter(security_safety__in=no_fire_line)
        no_tanks = EvaluationForm.objects.filter(security_safety__in=no_tanks)
        no_wall = EvaluationForm.objects.filter(security_safety__in=no_wall)
        no_analysis = EvaluationForm.objects.filter(administration__in=no_analysis)
        no_risks_indicators = EvaluationForm.objects.filter(administration__in=no_risks_indicators)
        no_transferred_files = EvaluationForm.objects.filter(students_affairs__in=no_transferred_files)
        no_labs_health_procedures = EvaluationForm.objects.filter(environment_population__in=no_labs_health_procedures)
        no_diagnosis_health_plan = EvaluationForm.objects.filter(environment_population__in=no_diagnosis_health_plan)
        no_toilets_health_procedures = EvaluationForm.objects.filter(environment_population__in=no_toilets_health_procedures)

        no_daily_received = SchoolStaticsSerializer(no_daily_received, many=True)
        no_health_certificate = SchoolStaticsSerializer(no_health_certificate, many=True)
        not_stored_periods = SchoolStaticsSerializer(not_stored_periods, many=True)
        no_training_plan = SchoolStaticsSerializer(no_training_plan, many=True)
        no_teachers_training = SchoolStaticsSerializer(no_teachers_training, many=True)
        no_fire_line = SchoolStaticsSerializer(no_fire_line, many=True)
        no_tanks = SchoolStaticsSerializer(no_tanks, many=True)
        no_wall = SchoolStaticsSerializer(no_wall, many=True)
        no_analysis = SchoolStaticsSerializer(no_analysis, many=True)
        no_risks_indicators = SchoolStaticsSerializer(no_risks_indicators, many=True)
        no_transferred_files = SchoolStaticsSerializer(no_transferred_files, many=True)
        no_labs_health_procedures = SchoolStaticsSerializer(no_labs_health_procedures, many=True)
        no_diagnosis_health_plan = SchoolStaticsSerializer(no_diagnosis_health_plan, many=True)
        no_toilets_health_procedures = SchoolStaticsSerializer(no_toilets_health_procedures, many=True)

        data = {
            'schools_with_issues': schools_with_issues.data,
            'schools_without_issues': schools_without_issues.data,
            'daily_not_received': no_daily_received.data,
            'no_health_certificate': no_health_certificate.data,
            'not_stored_periods': not_stored_periods.data,
            'no_training_plan': no_training_plan.data,
            'no_teachers_training': no_teachers_training.data,
            'no_fire_line': no_fire_line.data,
            'no_tanks': no_tanks.data,
            'no_wall': no_wall.data,
            'no_analysis': no_analysis.data,
            'no_risks_indicators': no_risks_indicators.data,
            'no_transferred_files': no_transferred_files.data,
            'no_labs_health_procedures': no_labs_health_procedures.data,
            'no_diagnosis_health_plan': no_diagnosis_health_plan.data,
            'no_toilets_health_procedures': no_toilets_health_procedures.data,
        }
        return Response(data)