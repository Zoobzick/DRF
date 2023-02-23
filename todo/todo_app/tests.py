import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import Mixer
from django.contrib.auth.models import User
from .views import TodoModelViewSet, ProjectsModelViewSet
from users.views import CustomUserModelViewSet
from .models import Todo, Projects
from users.models import CustomUser


class TestCases(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        admin = CustomUser.objects.create_superuser('admin', 'admin@mail.ru',
                                                    'admin')
        request = factory.get('/api/todo/')
        force_authenticate(request, admin)
        view = TodoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_projects(self):
        project = Projects.objects.create(
            name='test_project', repo_link='test_link')
        admin = CustomUser.objects.create_superuser(
            'admin', 'admin@mail.ru', 'admin')
        project.users.add(admin)
        project.save()
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProjectsViewSet(APITestCase):

    def test_edit_projects(self):
        admin = CustomUser.objects.create_superuser('admin', 'admin@mail.ru',
                                                    'admin')
        project = Projects.objects.create(
            name='test_name', repo_link='test_repo')
        project.users.add(admin)
        project.save()

        self.client.login(username='admin', password='admin')

        response = self.client.patch(f"/api/projects/{project.id}/", {
            "name": 'replaced_name', "repo_link": "replaced_link"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Projects.objects.get(id=project.id)

        self.assertEqual(project.name, 'replaced_name')
        self.assertEqual(project.repo_link, 'replaced_link')
