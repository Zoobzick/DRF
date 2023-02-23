import graphene
from graphene_django import DjangoObjectType
from .models import Todo, Projects
from ..users.models import CustomUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Projects.objects.all()


schema = graphene.Schema(query=Query)
