from .models import Todo, Projects
from rest_framework.serializers import HyperlinkedModelSerializer


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
