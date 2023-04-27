from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from EvaluateHub.serializers import IssueSerializer, ResponseSerializer, ClassRecordSerializer,MaterialSerializer, SecurityFactorsSerializer
from EvaluateHub.models import *
from EvaluateHub.validators import create_response_if_not_empty, update_response_if_not_empty
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