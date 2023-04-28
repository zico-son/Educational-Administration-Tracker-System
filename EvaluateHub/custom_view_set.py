from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin

class NoPostViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass

class NoUpdateViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin):
    pass