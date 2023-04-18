from rest_framework.serializers import ModelSerializer
from django.conf import settings
from EvaluateHub.models import * 
from core.models import User
class QualitySerializer(ModelSerializer):
    class Meta:
        model = Quality
        fields = '__all__'
class ClassRecordSerializer(ModelSerializer):
    class Meta:
        model = ClassRecord
        fields = ['registered', 'present', 'absent']

class StudentsAffairsSerializer(ModelSerializer):
    first_class = ClassRecordSerializer()
    # second_class = ClassRecordSerializer()
    # third_class = ClassRecordSerializer()
    class Meta:
        model = StudentsAffairs
        fields = ['first_class', 'transfers_to_school', 'transfers_from_school', 'transferred_files']

class SecurityFactorsSerializer(ModelSerializer):
    class Meta:
        model = SecurityFactors
        fields = '__all__'
class SecuritySafetySerializer(ModelSerializer):
    security_factors = SecurityFactorsSerializer()
    class Meta:
        model = SecuritySafety
        fields = ['id','labs','cabins', 'building','wall','external_factors','security_factors']

class StrategicPlanningSerializer(ModelSerializer):
    class Meta:
        model = StrategicPlanning
        fields = '__all__'

class AdministrationSerializer(ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'

class WorkersAffairsSerializer(ModelSerializer):
    class Meta:
        model = WorkersAffairs
        fields = '__all__'
class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class TrainingSerializer(ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class TeachersSerializer(ModelSerializer):
    material_one = MaterialSerializer()
    class Meta:
        model = Teachers
        fields = ['material_one']

class NutritionSerializer(ModelSerializer):
    class Meta:
        model = Nutrition
        fields = '__all__'
class DecentralizationSerializer(ModelSerializer):
    class Meta:
        model = Decentralization
        fields = '__all__'
class CooperativeSerializer(ModelSerializer):
    class Meta:
        model = Cooperative
        fields = '__all__'
class LaboratoriesSerializer(ModelSerializer):
    class Meta:
        model = Laboratories
        fields = '__all__'
class ProductionUnitSerializer(ModelSerializer):
    class Meta:
        model = ProductionUnit
        fields = '__all__'
class EnvironmentPopulationSerializer(ModelSerializer):
    class Meta:
        model = EnvironmentPopulation
        fields = '__all__'

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
        fields = ['id', 'school_name', 'school_id', 'school_level','security_safety', 'teachers','students_affairs', 'workers_affairs', 'strategic_planning', 'administration', 'training', 'nutrition', 'cooperative', 'laboratories', 'decentralization', 'production_unit', 'environment_population', 'quality', 'security_safety', 'teachers']
    def create(self, validated_data):
        students_affairs_data = validated_data.pop('students_affairs')
        first_class_data = students_affairs_data.pop('first_class')
        first_class = ClassRecord.objects.create(**first_class_data)
        students_affairs =StudentsAffairs.objects.create( first_class=first_class, **students_affairs_data)

        security_safety_data =validated_data.pop('security_safety')
        security_factors_data = security_safety_data.pop('security_factors')
        security_factors = SecurityFactors.objects.create(**security_factors_data)
        security_safety = SecuritySafety.objects.create(security_factors= security_factors,**security_safety_data)

        teachers_data = validated_data.pop('teachers')
        material_one_data = teachers_data.pop('material_one')
        material_one = Material.objects.create(**material_one_data)
        teachers = Teachers.objects.create(material_one = material_one, **teachers_data)

        workers_affairs_data = validated_data.pop('workers_affairs')
        workers_affairs = WorkersAffairs.objects.create(**workers_affairs_data)

        strategic_planning_data = validated_data.pop('strategic_planning')
        strategic_planning = StrategicPlanning.objects.create(**strategic_planning_data)
        
        administration_data = validated_data.pop('administration')
        administration = Administration.objects.create(**administration_data)
        
        training_data = validated_data.pop('training')
        training = Training.objects.create(**training_data)
        
        nutrition_data = validated_data.pop('nutrition')
        nutrition = Nutrition.objects.create(**nutrition_data)
        
        cooperative_data = validated_data.pop('cooperative')    
        cooperative = Cooperative.objects.create(**cooperative_data)
        
        laboratories_data = validated_data.pop('laboratories')
        laboratories = Laboratories.objects.create(**laboratories_data)
        
        decentralization_data = validated_data.pop('decentralization')
        decentralization = Decentralization.objects.create(**decentralization_data)
        
        production_unit_data = validated_data.pop('production_unit')
        production_unit = ProductionUnit.objects.create(**production_unit_data)
        
        environment_population_data = validated_data.pop('environment_population')
        environment_population = EnvironmentPopulation.objects.create(**environment_population_data)
        
        quality_data = validated_data.pop('quality')
        quality = Quality.objects.create(**quality_data)

        user_id =self.context['user_id']
        print (user_id)
        created_by = User.objects.get(pk=user_id)

        evaluation_form = EvaluationForm.objects.create(students_affairs=students_affairs, workers_affairs=workers_affairs, strategic_planning=strategic_planning, administration=administration, training=training, nutrition=nutrition, cooperative=cooperative, laboratories=laboratories, decentralization=decentralization, production_unit=production_unit, environment_population=environment_population, quality=quality,security_safety=security_safety,teachers = teachers, created_by =created_by,**validated_data)
        return evaluation_form
