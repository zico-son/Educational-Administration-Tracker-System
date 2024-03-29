from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.db import transaction
from django.conf import settings
from EvaluateHub.models import * 
from core.models import User
from EvaluateHub.utils import create_issue_if_not_empty, issue_checker, counter_checker
import inflect
class ClassRecordSerializer(ModelSerializer):
    class Meta:
        model = ClassRecord
        fields = ['registered', 'present', 'absent', 'level']

class ClassRecordViewSerializer(ModelSerializer):
    class Meta:
        model = ClassRecord
        fields = ['registered', 'present', 'absent']

class ResponseSerializer(ModelSerializer):
    class Meta:
        model =StudentAffairsResponse
        fields = ['response']

class IssueSerializer(ModelSerializer):
    class Meta:
        model =StudentAffairsIssue
        fields = ['issue']

class AdminStudentsAffairsSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    first_class = ClassRecordSerializer()
    class Meta:
        model = StudentsAffairs
        fields = ['first_class', 'transfers_to_school', 'transfers_from_school', 'transferred_files', 'issue', 'response']


class StudentsAffairsViewSerializer(ModelSerializer):
    first_class = ClassRecordViewSerializer()
    second_class = ClassRecordViewSerializer()
    third_class = ClassRecordViewSerializer()
    fourth_class = ClassRecordViewSerializer()
    fifth_class = ClassRecordViewSerializer()
    sixth_class = ClassRecordViewSerializer()
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True)
    class Meta:
        model = StudentsAffairs
        fields = ['id','first_class','second_class', 'third_class', 'fourth_class', 'fifth_class', 'sixth_class','transfers_to_school', 'transfers_from_school', 'transferred_files', 'issue', 'response' ]
class StudentsAffairsSerializer(ModelSerializer):
    first_class = ClassRecordSerializer()
    second_class = ClassRecordSerializer()
    third_class = ClassRecordSerializer()
    fourth_class = ClassRecordSerializer()
    fifth_class = ClassRecordSerializer()
    sixth_class = ClassRecordSerializer()
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True)
    class Meta:
        model = StudentsAffairs
        fields = ['id','first_class','second_class', 'third_class', 'fourth_class', 'fifth_class', 'sixth_class','transfers_to_school', 'transfers_from_school', 'transferred_files', 'issue', 'response' ]

class SecurityFactorsSerializer(ModelSerializer):
    class Meta:
        model = SecurityFactors
        fields = '__all__'

class SecuritySafetySerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    security_factors = SecurityFactorsSerializer()
    class Meta:
        model = SecuritySafety
        fields = ['id','labs','cabins', 'building','wall','external_factors','security_factors', 'issue', 'response']

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = ['name', 'increase', 'decrease'] 

class TeachersSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    material_one = MaterialSerializer()
    material_two = MaterialSerializer()
    material_three = MaterialSerializer()
    material_four = MaterialSerializer()
    material_five = MaterialSerializer()
    material_six = MaterialSerializer()
    material_seven = MaterialSerializer()
    material_eight = MaterialSerializer()
    material_nine = MaterialSerializer()
    material_ten = MaterialSerializer()
    material_eleven = MaterialSerializer()
    material_twelve = MaterialSerializer()
    class Meta:
        model = Teachers
        fields = ['material_one', 'material_two', 'material_three', 'material_four', 'material_five', 'material_six', 'material_seven', 'material_eight', 'material_nine', 'material_ten', 'material_eleven', 'material_twelve', 'issue', 'response']

class StrategicPlanningSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = StrategicPlanning
        fields = ['id', 'obstacles', 'plan_activation','team_building','plan','analysis','issue', 'response']

class AdministrationSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Administration
        fields = ['id' ,'execution_plan','team_building','analysis','activities_activation','obstacles','predicted_crisis','communication_system','risks_indicators','plan','training_on_plan', 'issue', 'response']

class QualitySerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Quality
        fields = ['id','first_year_one', 'second_year_one', 'third_year_one', 'fourth_year_one', 'fifth_year_one', 'sixth_year_one', 'first_year_two', 'second_year_two', 'third_year_two', 'fourth_year_two', 'fifth_year_two', 'sixth_year_two', 'first_year_three', 'second_year_three', 'third_year_three', 'fourth_year_three', 'fifth_year_three', 'sixth_year_three', 'issue', 'response']

class WorkersAffairsSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = WorkersAffairs
        fields = ['id', 'registered', 'present','absent', 'negatives', 'issue', 'response'] 

class TrainingSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Training
        fields = ['id', 'teachers_training', 'training_plan','training_plan_activation', 'issue', 'response']

class NutritionSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Nutrition
        fields = ['id', 'daily_received', 'daily_served','disciplined_distribution','health_certificate', 'not_stored_periods', 'issue', 'response']
class DecentralizationSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Decentralization
        fields = ['id', 'board_of_trustees', 'decentralization_committee','settlement', 'exchange', 'plan' ,'append','issue', 'response']
class CooperativeSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Cooperative
        fields = ['id','existing_authorized_items','drag_running' , 'drag_profits', 'issue', 'response' ]
class LaboratoriesSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = Laboratories
        fields = ['id', 'work_validity','ory_association','networks','computers','evaluation', 'tilo',  'issue', 'response']
class ProductionUnitSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = ProductionUnit
        fields = ['id', 'profit_distribution','supply','activation','certified','issue', 'response']
class EnvironmentPopulationSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    class Meta:
        model = EnvironmentPopulation
        fields = ['id', 'toilets_health_procedures','health_file','diagnosis_health_plan','check_health_plan','activities' ,'labs_health_procedures','issue', 'response'] 

class EvaluationFormViewSerializer(ModelSerializer):
    students_affairs = StudentsAffairsViewSerializer()
    security_safety = SecuritySafetySerializer()
    teachers = TeachersSerializer()
    workers_affairs = WorkersAffairsSerializer()
    strategic_planning = StrategicPlanningSerializer()
    administration = AdministrationSerializer()
    training = TrainingSerializer()
    nutrition = NutritionSerializer()
    cooperative = CooperativeSerializer()
    laboratories = LaboratoriesSerializer()
    decentralization = DecentralizationSerializer()
    production_unit = ProductionUnitSerializer()
    environment_population = EnvironmentPopulationSerializer()
    quality = QualitySerializer()

    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','students_affairs','security_safety', 'teachers','workers_affairs', 'strategic_planning', 'administration', 'training', 'nutrition', 'cooperative', 'laboratories', 'decentralization', 'production_unit', 'environment_population', 'quality', 'security_safety', 'teachers']

class EvaluationFormSerializer(ModelSerializer):
    students_affairs = StudentsAffairsSerializer()
    security_safety = SecuritySafetySerializer()
    teachers = TeachersSerializer()
    workers_affairs = WorkersAffairsSerializer()
    strategic_planning = StrategicPlanningSerializer()
    administration = AdministrationSerializer()
    training = TrainingSerializer()
    nutrition = NutritionSerializer()
    cooperative = CooperativeSerializer()
    laboratories = LaboratoriesSerializer()
    decentralization = DecentralizationSerializer()
    production_unit = ProductionUnitSerializer()
    environment_population = EnvironmentPopulationSerializer()
    quality = QualitySerializer()

    class Meta:
        model = EvaluationForm
        fields = ['id', 'school_name', 'school_id', 'school_level','students_affairs','security_safety', 'teachers','workers_affairs', 'strategic_planning', 'administration', 'training', 'nutrition', 'cooperative', 'laboratories', 'decentralization', 'production_unit', 'environment_population', 'quality', 'security_safety', 'teachers']


    def create(self, validated_data):
        with transaction.atomic():
            counter = 0
            ordinal_mapping = {
                1: 'first',
                2: 'second',
                3: 'third',
                4: 'fourth',
                5: 'fifth',
                6: 'sixth',
                7: 'seventh',
                8: 'eighth',
                9: 'ninth',
                10: 'tenth',
                11: 'eleventh',
                12: 'twelfth'
                }
            students_affairs_data = validated_data.pop('students_affairs')
            classes_data = {}
            for i in range(1, 7):
                class_data = students_affairs_data.pop(f'{ordinal_mapping.get(i)}_class')
                if class_data.get('registered') is not None:
                    class_data = ClassRecord.objects.create(**class_data)
                    classes_data[f'{ordinal_mapping.get(i)}_class'] = class_data
            print (classes_data)
            issue_data = students_affairs_data.pop('issue')
            students_affairs =StudentsAffairs.objects.create( **classes_data, **students_affairs_data)
            issue = create_issue_if_not_empty(issue_data, StudentAffairsIssue, students_affairs)
            counter = issue_checker(issue, counter)
            
            security_safety_data =validated_data.pop('security_safety')
            security_factors_data = security_safety_data.pop('security_factors')
            security_factors = SecurityFactors.objects.create(**security_factors_data)
            issue_data = security_safety_data.pop('issue')
            security_safety = SecuritySafety.objects.create(security_factors= security_factors,**security_safety_data)
            issue = create_issue_if_not_empty(issue_data, SecuritySafetyIssue, security_safety)
            counter = issue_checker(issue, counter)

            engine = inflect.engine()
            teachers_data = validated_data.pop('teachers')
            materials_data = {}
            for i in range(1, 13):
                material_data = teachers_data.pop(f'material_{engine.number_to_words(i)}')
                if material_data.get('decrease') is not None and material_data.get('increase') is not None:
                    material = Material.objects.create(**material_data)
                    materials_data[f'material_{engine.number_to_words(i)}'] = material
            issue_data = teachers_data.pop('issue')
            teachers = Teachers.objects.create(**teachers_data, **materials_data)
            issue = create_issue_if_not_empty(issue_data, TeachersIssue, teachers)
            counter = issue_checker(issue, counter)

            workers_affairs_data = validated_data.pop('workers_affairs')
            issue_data = workers_affairs_data.pop('issue')
            workers_affairs = WorkersAffairs.objects.create(**workers_affairs_data)
            issue = create_issue_if_not_empty(issue_data, WorkersAffairsIssue, workers_affairs)
            counter = issue_checker(issue, counter)

            strategic_planning_data = validated_data.pop('strategic_planning')
            issue_data = strategic_planning_data.pop('issue')
            strategic_planning = StrategicPlanning.objects.create(**strategic_planning_data)
            issue = create_issue_if_not_empty(issue_data, StrategicPlanningIssue, strategic_planning)
            counter = issue_checker(issue, counter)
            administration_data = validated_data.pop('administration')
            issue_data = administration_data.pop('issue')
            administration = Administration.objects.create(**administration_data)
            issue = create_issue_if_not_empty(issue_data, AdministrationIssue, administration)
            counter = issue_checker(issue, counter)
            training_data = validated_data.pop('training')
            issue_data = training_data.pop('issue')
            training = Training.objects.create(**training_data)
            issue = create_issue_if_not_empty(issue_data, TrainingIssue, training)
            counter = issue_checker(issue, counter)
            nutrition_data = validated_data.pop('nutrition')
            issue_data = nutrition_data.pop('issue')
            nutrition = Nutrition.objects.create(**nutrition_data)
            issue = create_issue_if_not_empty(issue_data, NutritionIssue, nutrition)
            counter = issue_checker(issue, counter)
            cooperative_data = validated_data.pop('cooperative')
            issue_data = cooperative_data.pop('issue')    
            cooperative = Cooperative.objects.create(**cooperative_data)
            issue = create_issue_if_not_empty(issue_data, CooperativeIssue, cooperative)
            counter = issue_checker(issue, counter)
            laboratories_data = validated_data.pop('laboratories')
            issue_data = laboratories_data.pop('issue')
            laboratories = Laboratories.objects.create(**laboratories_data)
            issue = create_issue_if_not_empty(issue_data, LaboratoriesIssue, laboratories)
            counter = issue_checker(issue, counter)
            decentralization_data = validated_data.pop('decentralization')
            issue_data = decentralization_data.pop('issue')
            decentralization = Decentralization.objects.create(**decentralization_data)
            issue = create_issue_if_not_empty(issue_data, DecentralizationIssue, decentralization)
            counter = issue_checker(issue, counter)
            production_unit_data = validated_data.pop('production_unit')
            issue_data = production_unit_data.pop('issue')
            production_unit = ProductionUnit.objects.create(**production_unit_data)
            issue = create_issue_if_not_empty(issue_data, ProductionUnitIssue, production_unit)
            counter = issue_checker(issue, counter)
            environment_population_data = validated_data.pop('environment_population')
            issue_data = environment_population_data.pop('issue')
            environment_population = EnvironmentPopulation.objects.create(**environment_population_data)
            issue = create_issue_if_not_empty(issue_data, EnvironmentPopulationIssue, environment_population)
            counter = issue_checker(issue, counter)
            quality_data = validated_data.pop('quality')
            issue_data = quality_data.pop('issue')
            quality = Quality.objects.create(**quality_data)
            issue = create_issue_if_not_empty(issue_data, QualityIssue, quality)
            counter = issue_checker(issue, counter)
            user_id =self.context['user_id']
            print (user_id)
            created_by = User.objects.get(pk=user_id)

            issues = counter_checker(counter)
            evaluation_form = EvaluationForm.objects.create(students_affairs=students_affairs, workers_affairs=workers_affairs, strategic_planning=strategic_planning, administration=administration, training=training, nutrition=nutrition, cooperative=cooperative, laboratories=laboratories, decentralization=decentralization, production_unit=production_unit, environment_population=environment_population, quality=quality,security_safety=security_safety,teachers = teachers, created_by =created_by, issues=issues, **validated_data) 
            return evaluation_form



class CreatedBySerializer(Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class EvaluationFormInfoSerializer(ModelSerializer):
    created_by = CreatedBySerializer()
    class Meta:
        model = EvaluationForm
        fields = ['school_name', 'school_id', 'school_level', 'created_at', 'created_by']

class SecurityFactorsStaticsSerializer(serializers.Serializer):
    fire_line_valid = serializers.IntegerField()
    fire_line_invalid = serializers.IntegerField()
    tanks_valid = serializers.IntegerField()
    tanks_invalid = serializers.IntegerField()
    buckets_valid = serializers.IntegerField()
    buckets_invalid = serializers.IntegerField()
    fire_extinguishers_valid = serializers.IntegerField()
    fire_extinguishers_invalid = serializers.IntegerField()

class SecuritySafetyStaticsSerializer(serializers.Serializer):
    labs_disciplined = serializers.IntegerField()
    labs_undisciplined = serializers.IntegerField()
    cabins_disciplined = serializers.IntegerField()
    cabins_undisciplined = serializers.IntegerField()
    building_disciplined = serializers.IntegerField()
    building_undisciplined = serializers.IntegerField()
    wall_disciplined = serializers.IntegerField()
    wall_undisciplined = serializers.IntegerField()
    external_factors_disciplined = serializers.IntegerField()
    external_factors_undisciplined = serializers.IntegerField()

class StrategicPlanningStaticsSerializer(serializers.Serializer):
    obstacles_exits = serializers.IntegerField()
    obstacles_noexist = serializers.IntegerField()
    plan_activation_exits = serializers.IntegerField()
    plan_activation_noexist = serializers.IntegerField()
    team_building_exits = serializers.IntegerField()
    team_building_noexist = serializers.IntegerField()
    plan_exits = serializers.IntegerField()
    plan_noexist = serializers.IntegerField()
    analysis_exits = serializers.IntegerField()
    analysis_noexist = serializers.IntegerField()
class AdministrationStaticsSerializer(serializers.Serializer):
    execution_plan_exits = serializers.IntegerField()
    execution_plan_noexist = serializers.IntegerField()
    team_building_exits = serializers.IntegerField()
    team_building_noexist = serializers.IntegerField()
    analysis_exits = serializers.IntegerField()
    analysis_noexist = serializers.IntegerField()
    activities_activation_exits = serializers.IntegerField()
    activities_activation_noexist = serializers.IntegerField()
    obstacles_exits = serializers.IntegerField()
    obstacles_noexist = serializers.IntegerField()
    predicted_crisis_exits = serializers.IntegerField()
    predicted_crisis_noexist = serializers.IntegerField()
    communication_system_exits = serializers.IntegerField()
    communication_system_noexist = serializers.IntegerField()
    risks_indicators_exits = serializers.IntegerField()
    risks_indicators_noexist = serializers.IntegerField()
    plan_exits = serializers.IntegerField()
    plan_noexist = serializers.IntegerField()
    training_on_plan_exits = serializers.IntegerField()
    training_on_plan_noexist = serializers.IntegerField()

class TrainingStaticsSerializer(serializers.Serializer):
    teachers_training_exits = serializers.IntegerField()
    teachers_training_noexist = serializers.IntegerField()
    training_plan_exits = serializers.IntegerField()
    training_plan_noexist = serializers.IntegerField()
    training_plan_activation_exits = serializers.IntegerField()
    training_plan_activation_noexist = serializers.IntegerField()

class NutritionStaticsSerializer(serializers.Serializer):
    daily_received_exits = serializers.IntegerField()
    daily_received_noexist = serializers.IntegerField()
    daily_served_exits = serializers.IntegerField()
    daily_served_noexist = serializers.IntegerField()
    disciplined_distribution_exits = serializers.IntegerField()
    disciplined_distribution_noexist = serializers.IntegerField()
    health_certificate_exits = serializers.IntegerField()
    health_certificate_noexist = serializers.IntegerField()
    not_stored_periods_exits = serializers.IntegerField()
    not_stored_periods_noexist = serializers.IntegerField()


class DecentralizationStaticsSerializer(serializers.Serializer):
    board_of_trustees_exits = serializers.IntegerField()
    board_of_trustees_noexist = serializers.IntegerField()
    decentralization_committee_exits = serializers.IntegerField()
    decentralization_committee_noexist = serializers.IntegerField()
    settlement_exits = serializers.IntegerField()
    settlement_noexist = serializers.IntegerField()
    exchange_exits = serializers.IntegerField()
    exchange_noexist = serializers.IntegerField()
    plan_exits = serializers.IntegerField()
    plan_noexist = serializers.IntegerField()
    append_exits = serializers.IntegerField()
    append_noexist = serializers.IntegerField()

class CooperativeStaticsSerializer(serializers.Serializer):
    existing_authorized_items_exits = serializers.IntegerField()
    existing_authorized_items_noexist = serializers.IntegerField()
    drag_running_exits = serializers.IntegerField()
    drag_running_noexist = serializers.IntegerField()
    drag_profits_exits = serializers.IntegerField()
    drag_profits_noexist = serializers.IntegerField()


class LaboratoriesStaticsSerializer(serializers.Serializer):
    work_validity_exits = serializers.IntegerField()
    work_validity_noexist = serializers.IntegerField()
    ory_association = serializers.IntegerField()
    networks = serializers.IntegerField()
    computers = serializers.IntegerField()
    evaluation = serializers.IntegerField()
    tilo = serializers.IntegerField()



class ProductionUnitStaticsSerializer(serializers.Serializer):
    profit_distribution_exits = serializers.IntegerField()
    profit_distribution_noexist = serializers.IntegerField()
    supply_exits = serializers.IntegerField()
    supply_noexist = serializers.IntegerField()
    activation_exits = serializers.IntegerField()
    activation_noexist = serializers.IntegerField()
    certified_exits = serializers.IntegerField()
    certified_noexist = serializers.IntegerField()



class EnvironmentPopulationStaticsSerializer(serializers.Serializer):
    toilets_health_procedures_exits = serializers.IntegerField()
    toilets_health_procedures_noexist = serializers.IntegerField()
    health_file_exits = serializers.IntegerField()
    health_file_noexist = serializers.IntegerField()
    diagnosis_health_plan_exits = serializers.IntegerField()
    diagnosis_health_plan_noexist = serializers.IntegerField()
    check_health_plan_exits = serializers.IntegerField()
    check_health_plan_noexist = serializers.IntegerField()
    activities_exits = serializers.IntegerField()
    activities_noexist = serializers.IntegerField()
    labs_health_procedures_exits = serializers.IntegerField()
    labs_health_procedures_noexist = serializers.IntegerField()

class WorkersAffairsStaticsSerializer(serializers.Serializer):
    percentage_of_absence_gt_10 = serializers.IntegerField()
    percentage_of_absence_gt_20 = serializers.IntegerField()
    percentage_of_absence_gt_30 = serializers.IntegerField()
    percentage_of_absence_gt_40 = serializers.IntegerField()
    percentage_of_absence_gt_50 = serializers.IntegerField()

class StudentsAffairsStaticsSerializer(serializers.Serializer):
    percentage_of_absence_primary = serializers.FloatField()
    percentage_of_absence_intermediate = serializers.FloatField()
    percentage_of_absence_secondary = serializers.FloatField()
    percentage_of_registered_primary = serializers.FloatField()
    percentage_of_registered_intermediate = serializers.FloatField()
    percentage_of_registered_secondary = serializers.FloatField()


class SchoolStaticsSerializer(serializers.Serializer):
    school_name = serializers.CharField()
    school_level = serializers.CharField()