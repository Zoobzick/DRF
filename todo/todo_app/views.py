from rest_framework.viewsets import ModelViewSet
from .models import Todo, Projects
from .serializers import TodoModelSerializer, ProjectsModelSerializer, TodoModelSerializerBase
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination

    # def get_queryset(self):
    #     param = self.request.query_params.get('project_id')
    #     if param:
    #         return Todo.objects.filter(project_id=param)
    #     return super().get_queryset()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        inactive = {'is_active': False}
        TodoModelSerializer(instance).update(instance, inactive)
        return Response({'TODO task was set to Inactive'})

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoModelSerializer
        return TodoModelSerializerBase


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer
    pagination_class = ProjectsLimitOffsetPagination

    def get_queryset(self):
        param = self.request.query_params.get('name')
        if param is not None:
            projects = Projects.objects.filter(name__contains=param)
            return projects
        return super().get_queryset()
