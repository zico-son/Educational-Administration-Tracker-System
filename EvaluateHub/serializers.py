from rest_framework.serializers import ModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer as NestedSerializer
from EvaluateHub.models import *


class ClassRecordSerializer(ModelSerializer):
    class Meta:
        model = ClassRecord
        fields = ['registered', 'present', 'absent']

class StudentsAffairsSerializer(NestedSerializer):
    first_class = ClassRecordSerializer()
    second_class = ClassRecordSerializer()
    third_class = ClassRecordSerializer()
    class Meta:
        model = StudentsAffairs
        fields = ['first_class', 'second_class', 'third_class', 'transfers_to_school', 'transfers_from_school', 'transferred_files']