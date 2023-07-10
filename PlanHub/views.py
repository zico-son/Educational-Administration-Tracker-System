from rest_framework.viewsets import ModelViewSet
from PlanHub.models import Plan
from PlanHub.serializers import ManagerPlanSerializer, DepartmentPlanSerializer, ManagerPlanViewSerializer
from PlanHub.custom_view_set import NoPostViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend



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
    queryset = Plan.objects.prefetch_related('activities').all()
    serializer_class = DepartmentPlanSerializer
    def get_serializer_context(self):
        return {'department': self.request.user.role}
