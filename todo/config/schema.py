import graphene
from graphene_django import DjangoObjectType
from todo_app.models import Todo, Projects
from users.models import CustomUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(CustomUserType)
    all_todos = graphene.List(TodoType)
    project_by_name = graphene.List(
        ProjectType, name=graphene.String(required=True))

    def resolve_all_projects(root, info):
        return Projects.objects.all()

    def resolve_all_users(root, info):
        return CustomUser.objects.all()

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_project_by_name(root, info, name):
        try:
            return Projects.objects.filter(name=name)
        except Projects.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
