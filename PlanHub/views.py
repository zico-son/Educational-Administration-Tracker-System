from rest_framework.viewsets import ModelViewSet
from PlanHub.models import Plan, Activities
from PlanHub.serializers import ManagerPlanSerializer, DepartmentPlanSerializer, ManagerPlanViewSerializer, PostFileSerializer, ActivitiesSerializer
from PlanHub.custom_view_set import NoPostViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status



class ManagerPlanViewSet(NoPostViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department', 'approved', 'done', 'archived'] 
    queryset = Plan.objects.prefetch_related('activities').all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ManagerPlanViewSerializer
        return ManagerPlanSerializer 
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer = ManagerPlanViewSerializer(instance)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class DepartmentPlanViewSet(ModelViewSet):
    
    serializer_class = DepartmentPlanSerializer
    def get_serializer_context(self):
        return {'department': self.request.user.role}
    def get_queryset(self):
        return Plan.objects.prefetch_related('activities').filter(department = self.request.user.role.replace('_', ' ').replace('admin', '').strip())

class PostFileViewSet(ModelViewSet):
    def get_queryset(self):
        return Activities.objects.none()
    serializer_class = PostFileSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = ActivitiesSerializer(serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)