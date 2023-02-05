from .models import Todo, Projects
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):
    project = ProjectsModelSerializer(source='project_id')

    class Meta:
        model = Todo
        fields = '__all__'
