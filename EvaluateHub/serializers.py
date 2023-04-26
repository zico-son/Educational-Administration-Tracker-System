from rest_framework.serializers import ModelSerializer
from django.db import transaction
from django.conf import settings
from EvaluateHub.models import * 
from core.models import User
from .validators import create_issue_if_not_empty

class ClassRecordSerializer(ModelSerializer):
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

class StudentsAffairsSerializer(ModelSerializer):
    first_class = ClassRecordSerializer()
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True)
    class Meta:
        model = StudentsAffairs
        fields = ['id','first_class', 'transfers_to_school', 'transfers_from_school', 'transferred_files', 'issue', 'response']

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
        fields = '__all__'

class TeachersSerializer(ModelSerializer):
    issue = IssueSerializer()
    response = ResponseSerializer(read_only = True) 
    material_one = MaterialSerializer()
    class Meta:
        model = Teachers
        fields = ['material_one', 'issue', 'response']

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
        fields = ['id','first_year_one','second_year_one', 'third_year_one', 'first_year_two', 'second_year_two', 'third_year_two', 'first_year_three', 'second_year_three', 'third_year_three','issue', 'response']

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
        fields = ['id', 'work_validity','networks','computers','evaluation', 'tilo',  'issue', 'response']
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
            students_affairs_data = validated_data.pop('students_affairs')
            first_class_data = students_affairs_data.pop('first_class')
            first_class = ClassRecord.objects.create(**first_class_data)
            issue_data = students_affairs_data.pop('issue')
            students_affairs =StudentsAffairs.objects.create( first_class=first_class, **students_affairs_data)
            create_issue_if_not_empty(issue_data, StudentAffairsIssue, students_affairs)
            
            security_safety_data =validated_data.pop('security_safety')
            security_factors_data = security_safety_data.pop('security_factors')
            security_factors = SecurityFactors.objects.create(**security_factors_data)
            issue_data = security_safety_data.pop('issue')
            security_safety = SecuritySafety.objects.create(security_factors= security_factors,**security_safety_data)
            create_issue_if_not_empty(issue_data, SecuritySafetyIssue, security_safety)

            teachers_data = validated_data.pop('teachers')
            material_one_data = teachers_data.pop('material_one')
            material_one = Material.objects.create(**material_one_data)
            issue_data = teachers_data.pop('issue')
            teachers = Teachers.objects.create(material_one = material_one, **teachers_data)
            create_issue_if_not_empty(issue_data, TeachersIssue, teachers)

            workers_affairs_data = validated_data.pop('workers_affairs')
            issue_data = workers_affairs_data.pop('issue')
            workers_affairs = WorkersAffairs.objects.create(**workers_affairs_data)
            create_issue_if_not_empty(issue_data, WorkersAffairsIssue, workers_affairs)

            strategic_planning_data = validated_data.pop('strategic_planning')
            issue_data = strategic_planning_data.pop('issue')
            strategic_planning = StrategicPlanning.objects.create(**strategic_planning_data)
            create_issue_if_not_empty(issue_data, StrategicPlanningIssue, strategic_planning)
            
            administration_data = validated_data.pop('administration')
            issue_data = administration_data.pop('issue')
            administration = Administration.objects.create(**administration_data)
            create_issue_if_not_empty(issue_data, AdministrationIssue, administration)
            
            training_data = validated_data.pop('training')
            issue_data = training_data.pop('issue')
            training = Training.objects.create(**training_data)
            create_issue_if_not_empty(issue_data, TrainingIssue, training)
            
            nutrition_data = validated_data.pop('nutrition')
            issue_data = nutrition_data.pop('issue')
            nutrition = Nutrition.objects.create(**nutrition_data)
            create_issue_if_not_empty(issue_data, NutritionIssue, nutrition)
            
            cooperative_data = validated_data.pop('cooperative')
            issue_data = cooperative_data.pop('issue')    
            cooperative = Cooperative.objects.create(**cooperative_data)
            create_issue_if_not_empty(issue_data, CooperativeIssue, cooperative)
            
            laboratories_data = validated_data.pop('laboratories')
            issue_data = laboratories_data.pop('issue')
            laboratories = Laboratories.objects.create(**laboratories_data)
            create_issue_if_not_empty(issue_data, LaboratoriesIssue, laboratories)
            
            decentralization_data = validated_data.pop('decentralization')
            issue_data = decentralization_data.pop('issue')
            decentralization = Decentralization.objects.create(**decentralization_data)
            create_issue_if_not_empty(issue_data, DecentralizationIssue, decentralization)
            
            production_unit_data = validated_data.pop('production_unit')
            issue_data = production_unit_data.pop('issue')
            production_unit = ProductionUnit.objects.create(**production_unit_data)
            create_issue_if_not_empty(issue_data, ProductionUnitIssue, production_unit)
            
            environment_population_data = validated_data.pop('environment_population')
            issue_data = environment_population_data.pop('issue')
            environment_population = EnvironmentPopulation.objects.create(**environment_population_data)
            create_issue_if_not_empty(issue_data, EnvironmentPopulationIssue, environment_population)
            
            quality_data = validated_data.pop('quality')
            issue_data = quality_data.pop('issue')
            quality = Quality.objects.create(**quality_data)
            create_issue_if_not_empty(issue_data, QualityIssue, quality)

            user_id =self.context['user_id']
            print (user_id)
            created_by = User.objects.get(pk=user_id)

            evaluation_form = EvaluationForm.objects.create(students_affairs=students_affairs, workers_affairs=workers_affairs, strategic_planning=strategic_planning, administration=administration, training=training, nutrition=nutrition, cooperative=cooperative, laboratories=laboratories, decentralization=decentralization, production_unit=production_unit, environment_population=environment_population, quality=quality,security_safety=security_safety,teachers = teachers, created_by =created_by,**validated_data)
            return evaluation_form