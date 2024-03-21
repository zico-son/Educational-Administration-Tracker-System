from django.db import transaction
from rest_framework.serializers import ModelSerializer, CharField
from PlanHub.models import Plan, Activities


class ActivitiesSerializer(ModelSerializer):
    class Meta:
        model = Activities
        fields = ['id','activity', 'file']

class ManagerPlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['approved', 'done', 'archived']


class ManagerPlanViewSerializer(ModelSerializer):
    activities = ActivitiesSerializer(many=True)
    class Meta:
        model = Plan
        fields = ['id','objective', 'execution_time', 'department','executed_by', 'execution_tracker', 'activities', 'approved', 'done', 'archived']

class ActivitiesSerializer(ModelSerializer):
    class Meta:
        model = Activities
        fields = ['id','activity', 'file']
class DepartmentPlanSerializer(ModelSerializer):
    activities = ActivitiesSerializer(many=True)
    class Meta:
        model = Plan
        fields = ['id','objective', 'execution_time','executed_by', 'execution_tracker', 'activities', 'done']
        read_only_fields = ['done']
    
    def create(self, validated_data):
        with transaction.atomic():
            activities_data = validated_data.pop('activities')
            department = self.context['department']
            department = department.replace('_', ' ').replace('admin', '').strip()
            plan = Plan.objects.create(department = department,**validated_data)
            for activity_data in activities_data:
                Activities.objects.create(plan=plan, **activity_data)
            return plan

    def update(self, instance, validated_data):
        activities_data = validated_data.pop('activities')
        activities = instance.activities.all()

        # Perform partial update of the Plan model (instance)
        instance.objective = validated_data.get('objective', instance.objective)
        instance.execution_time = validated_data.get('execution_time', instance.execution_time)
        instance.executed_by = validated_data.get('executed_by', instance.executed_by)
        instance.execution_tracker = validated_data.get('execution_tracker', instance.execution_tracker)
        instance.done = validated_data.get('done', instance.done)
        instance.save()

        # Perform update for each activity
        for activity_data in activities_data:
            activity_id = activity_data.get('id', None)
            if activity_id:
                activity = activities.get(pk=activity_id)

                # Update activity fields
                activity.activity = activity_data.get('activity', activity.activity)

                # Update the file field if provided
                file = activity_data.get('file', None)
                if file:
                    activity.file = file

                activity.save()

        return instance



class PostFileSerializer(ModelSerializer):
    activity_id = CharField(max_length=8)
    class Meta:
        model = Activities
        fields = ['activity_id','file']
    
    def create(self, validated_data):
        activity_id = validated_data.pop('activity_id')
        activity = Activities.objects.get(pk=activity_id)
        activity.file = validated_data.get('file', activity.file)
        activity.save()
        return activity