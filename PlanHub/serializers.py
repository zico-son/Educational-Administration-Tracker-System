from django.db import transaction
from rest_framework.serializers import ModelSerializer
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
        with transaction.atomic():
            activities_data = validated_data.pop('activities', [])
            instance.objective = validated_data.get('objective', instance.objective)
            instance.execution_time = validated_data.get('execution_time', instance.execution_time)
            instance.executed_by = validated_data.get('executed_by', instance.executed_by)
            instance.execution_tracker = validated_data.get('execution_tracker', instance.execution_tracker)
            instance.save()

            # Update activities
            existing_activities = list(instance.activities.all())
            existing_activity_ids = [activity.id for activity in existing_activities]
            for activity_data in activities_data:
                activity_id = activity_data.get('id')
                if activity_id in existing_activity_ids:
                    activity = Activities.objects.get(id=activity_id)
                    activity.description = activity_data.get('description', activity.description)
                    activity.save()
                    existing_activities.remove(activity)
                else:
                    Activities.objects.create(plan=instance, **activity_data)

            # Delete any remaining activities that were not included in the update
            for activity in existing_activities:
                activity.delete()

            return instance

