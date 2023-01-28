from rest_framework.viewsets import ModelViewSet
from .models import Todo, Projects
from .serializers import TodoModelSerializer, ProjectsModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer
