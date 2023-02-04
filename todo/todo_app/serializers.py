from .models import Todo, Projects
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
