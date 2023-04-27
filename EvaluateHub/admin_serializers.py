from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from EvaluateHub.serializers import IssueSerializer, ResponseSerializer, ClassRecordSerializer,MaterialSerializer, SecurityFactorsSerializer
from EvaluateHub.models import *
from EvaluateHub.utils import create_response_if_not_empty, update_response_if_not_empty
from django.core.exceptions import ObjectDoesNotExist


class AdminStudentsAffairsSerializer(ModelSerializer):
    first_class = ClassRecordSerializer(read_only =True)
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer()
    class Meta:
        model = StudentsAffairs
        fields = ['id','first_class','transfers_to_school','transfers_from_school','transferred_files', 'issue','response']
        read_only_fields = ['id','first_class', 'transfers_to_school', 'transfers_from_school', 'transferred_files']


class AdminSecuritySafetySerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    security_factors = SecurityFactorsSerializer()
    class Meta:
        model = SecuritySafety
        fields = ['id','labs','cabins', 'building','wall','external_factors','security_factors', 'issue','response']
        read_only_fields = ['id','labs','cabins', 'building','wall','external_factors','security_factors', 'issue']

class AdminTeachersSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    material_one = MaterialSerializer()
    class Meta:
        model = Teachers
        fields = ['material_one', 'issue', 'response']
        read_only_fields = ['material_one', 'issue']

class AdminStrategicPlanningSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = StrategicPlanning
        fields = ['id', 'obstacles', 'plan_activation','team_building','plan','analysis','issue', 'response']
        read_only_fields = ['id', 'obstacles', 'plan_activation','team_building','plan','analysis','issue']

class AdminAdministrationSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Administration
        fields = ['id' ,'execution_plan','team_building','analysis','activities_activation','obstacles','predicted_crisis','communication_system','risks_indicators','plan','training_on_plan', 'issue', 'response']
        read_only_fields = ['id' ,'execution_plan','team_building','analysis','activities_activation','obstacles','predicted_crisis','communication_system','risks_indicators','plan','training_on_plan', 'issue']

class AdminQualitySerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Quality
        fields = ['id','first_year_one','second_year_one', 'third_year_one', 'first_year_two', 'second_year_two', 'third_year_two', 'first_year_three', 'second_year_three', 'third_year_three','issue', 'response']
        read_only_fields = ['id', 'first_year_one','second_year_one', 'third_year_one', 'first_year_two', 'second_year_two', 'third_year_two', 'first_year_three', 'second_year_three', 'third_year_three','issue']

class AdminWorkersAffairsSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = WorkersAffairs
        fields = ['id', 'registered', 'present','absent', 'negatives', 'issue', 'response']
        read_only_fields = ['id', 'registered', 'present','absent', 'negatives', 'issue']

class AdminTrainingSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Training
        fields = ['id', 'teachers_training', 'training_plan','training_plan_activation', 'issue', 'response']
        read_only_fields = ['id', 'teachers_training', 'training_plan','training_plan_activation', 'issue']

class AdminNutritionSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Nutrition
        fields = ['id', 'daily_received', 'daily_served','disciplined_distribution','health_certificate', 'not_stored_periods', 'issue', 'response']
        read_only_fields = ['id', 'daily_received', 'daily_served','disciplined_distribution','health_certificate', 'not_stored_periods', 'issue']

class AdminDecentralizationSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Decentralization
        fields = ['id', 'board_of_trustees', 'decentralization_committee','settlement', 'exchange', 'plan' ,'append','issue', 'response']
        read_only_fields=['id', 'board_of_trustees', 'decentralization_committee','settlement', 'exchange', 'plan' ,'append','issue']

class AdminCooperativeSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Cooperative
        fields = ['id','existing_authorized_items','drag_running' , 'drag_profits', 'issue', 'response' ]
        read_only_fields = ['id','existing_authorized_items','drag_running' , 'drag_profits', 'issue' ]

class AdminLaboratoriesSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = Laboratories
        fields = ['id', 'work_validity','networks','computers','evaluation', 'tilo',  'issue', 'response']
        read_only_fields = ['id', 'work_validity','networks','computers','evaluation', 'tilo',  'issue']

class AdminProductionUnitSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = ProductionUnit
        fields = ['id', 'profit_distribution','supply','activation','certified','issue', 'response']
        read_only_fields = ['id', 'profit_distribution','supply','activation','certified','issue']

class AdminEnvironmentPopulationSerializer(ModelSerializer):
    issue = IssueSerializer(read_only =True)
    response = ResponseSerializer() 
    class Meta:
        model = EnvironmentPopulation
        fields = ['id', 'toilets_health_procedures','health_file','diagnosis_health_plan','check_health_plan','activities' ,'labs_health_procedures','issue', 'response']
        read_only_fields = ['id', 'toilets_health_procedures','health_file','diagnosis_health_plan','check_health_plan','activities' ,'labs_health_procedures','issue']

class AdminStudentsEvaluationFormSerializer(ModelSerializer):
    students_affairs = AdminStudentsAffairsSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','students_affairs']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        students_affairs_data = validated_data.pop('students_affairs')
        response_data = students_affairs_data.pop('response')
        students_affairs = StudentsAffairs.objects.get(pk = instance.students_affairs.id)
        try:
            if instance.students_affairs.response:
                print (instance.students_affairs.response) 
                update_response_if_not_empty(response_data, StudentAffairsResponse, students_affairs)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, StudentAffairsResponse, students_affairs)
        instance.students_affairs = students_affairs
        return instance

class AdminWorkersEvaluationFormSerializer(ModelSerializer):
    workers_affairs = AdminWorkersAffairsSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','workers_affairs']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        workers_affairs_data = validated_data.pop('workers_affairs')
        response_data = workers_affairs_data.pop('response')
        workers_affairs = WorkersAffairs.objects.get(pk = instance.workers_affairs.id)
        try:
            if instance.workers_affairs.response:
                update_response_if_not_empty(response_data, WorkersAffairsResponse, workers_affairs)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, WorkersAffairsResponse, workers_affairs)
        instance.workers_affairs = workers_affairs
        return instance

class AdminTrainingEvaluationFormSerializer(ModelSerializer):
    training = AdminTrainingSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','training']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        training_data = validated_data.pop('training')
        response_data = training_data.pop('response')
        training = Training.objects.get(pk = instance.training.id)
        try:
            if instance.training.response:
                update_response_if_not_empty(response_data, TrainingResponse, training)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, TrainingResponse, training)
        instance.training = training
        return instance

class AdminNutritionEvaluationFormSerializer(ModelSerializer):
    nutrition = AdminNutritionSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','nutrition']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        nutrition_data = validated_data.pop('nutrition')
        response_data = nutrition_data.pop('response')
        nutrition = Nutrition.objects.get(pk = instance.nutrition.id)
        try:
            if instance.nutrition.response:
                update_response_if_not_empty(response_data, NutritionResponse, nutrition)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, NutritionResponse, nutrition)
        instance.nutrition = nutrition
        return instance

class AdminEnvironmentPopulationEvaluationFormSerializer(ModelSerializer):
    environment_population = AdminEnvironmentPopulationSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','environment_population']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        environment_data = validated_data.pop('environment_population')
        response_data = environment_data.pop('response')
        environment = EnvironmentPopulation.objects.get(pk = instance.environment.id)
        try:
            if instance.environment.response:
                update_response_if_not_empty(response_data, EnvironmentPopulationResponse, environment)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, EnvironmentPopulationResponse, environment)
        instance.environment = environment
        return instance
    
class AdminCooperativeEvaluationFormSerializer(ModelSerializer):
    cooperative = AdminCooperativeSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','cooperative']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        cooperative_data = validated_data.pop('cooperative')
        response_data = cooperative_data.pop('response')
        cooperative = Cooperative.objects.get(pk = instance.cooperative.id)
        try:
            if instance.cooperative.response:
                update_response_if_not_empty(response_data, CooperativeResponse, cooperative)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, CooperativeResponse, cooperative)
        instance.cooperative = cooperative
        return instance

class AdminProductionUnitEvaluationFormSerializer(ModelSerializer):
    production_unit = AdminProductionUnitSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','production_unit']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        production_unit_data = validated_data.pop('production_unit')
        response_data = production_unit_data.pop('response')
        production_unit = ProductionUnit.objects.get(pk = instance.production_unit.id)
        try:
            if instance.production_unit.response:
                update_response_if_not_empty(response_data, ProductionUnitResponse, production_unit)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, ProductionUnitResponse, production_unit)
        instance.production_unit = production_unit
        return instance

class AdminSecuritySafetyEvaluationFormSerializer(ModelSerializer):
    security_safety = AdminSecuritySafetySerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','security_safety']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        security_safety_data = validated_data.pop('security_safety')
        response_data = security_safety_data.pop('response')
        security_safety = SecuritySafety.objects.get(pk = instance.security_safety.id)
        try:
            if instance.security_safety.response:
                update_response_if_not_empty(response_data, SecuritySafetyResponse, security_safety)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, SecuritySafetyResponse, security_safety)
        instance.security_safety = security_safety
        return instance

class AdminTeachersEvaluationFormSerializer(ModelSerializer):
    teachers = AdminTeachersSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','teachers']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        teachers_data = validated_data.pop('teachers')
        response_data = teachers_data.pop('response')
        teachers = Teachers.objects.get(pk = instance.teachers.id)
        try:
            if instance.teachers.response:
                update_response_if_not_empty(response_data, TeachersResponse, teachers)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, TeachersResponse, teachers)
        instance.teachers = teachers
        return instance

class AdminStrategicPlanningEvaluationFormSerializer(ModelSerializer):
    strategic_planning = AdminStrategicPlanningSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','strategic_planning']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        strategic_planning_data = validated_data.pop('strategic_planning')
        response_data = strategic_planning_data.pop('response')
        strategic_planning = StrategicPlanning.objects.get(pk = instance.strategic_planning.id)
        try:
            if instance.strategic_planning.response:
                update_response_if_not_empty(response_data, StrategicPlanningResponse, strategic_planning)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, StrategicPlanningResponse, strategic_planning)
        instance.strategic_planning = strategic_planning
        return instance

class AdminAdministrationEvaluationFormSerializer(ModelSerializer):
    administration = AdminAdministrationSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','administration']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        administration_data = validated_data.pop('administration')
        response_data = administration_data.pop('response')
        administration = Administration.objects.get(pk = instance.administration.id)
        try:
            if instance.administration.response:
                update_response_if_not_empty(response_data, AdministrationResponse, administration)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, AdministrationResponse, administration)
        instance.administration = administration
        return instance

class AdminQualityEvaluationFormSerializer(ModelSerializer):
    quality = AdminQualitySerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','quality']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update (self, instance,validated_data):
        quality_data = validated_data.pop('quality')
        response_data = quality_data.pop('response')
        quality = Quality.objects.get(pk = instance.quality.id)
        try:
            if instance.quality.response:
                update_response_if_not_empty(response_data, QualityResponse, quality)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, QualityResponse, quality)
        instance.quality = quality
        return instance

class AdminDecentralizationEvaluationFormSerializer(ModelSerializer):
    decentralization = AdminDecentralizationSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','decentralization']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        decentralization_data = validated_data.pop('decentralization')
        response_data = decentralization_data.pop('response')
        decentralization = Decentralization.objects.get(pk = instance.decentralization.id)
        try:
            if instance.decentralization.response:
                update_response_if_not_empty(response_data, DecentralizationResponse, decentralization)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, DecentralizationResponse, decentralization)
        instance.decentralization = decentralization
        return instance

class AdminLaboratoriesEvaluationFormSerializer(ModelSerializer):
    laboratories = AdminLaboratoriesSerializer()
    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','laboratories']
        read_only_fields = ['id', 'school_name', 'school_id', 'school_level']

    def update(self, instance, validated_data):
        laboratories_data = validated_data.pop('laboratories')
        response_data = laboratories_data.pop('response')
        laboratories = Laboratories.objects.get(pk = instance.laboratories.id)
        try:
            if instance.laboratories.response:
                update_response_if_not_empty(response_data, LaboratoriesResponse, laboratories)
        except ObjectDoesNotExist:
                create_response_if_not_empty(response_data, LaboratoriesResponse, laboratories)
        instance.laboratories = laboratories
        return instance