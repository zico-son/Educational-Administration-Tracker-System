from rest_framework.serializers import ModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer as NestedSerializer
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

