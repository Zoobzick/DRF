from django.db import models
from users.models import CustomUser


class Projects(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        unique=True
    )
    repo_link = models.CharField(
        max_length=200,
        blank=True,
        unique=True
    )
    users = models.ManyToManyField(CustomUser)


class Todo(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    text = models.CharField(
        max_length=300,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_DEFAULT, default="inactive_user")
    is_active = models.BooleanField(default=True)
