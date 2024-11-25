from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tasks.models import Task


class TaskViewSetTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.task = Task.objects.create(
            user=self.user,
            title="Example title",
            description="Example description",
            expiration_date=datetime.now(),
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse("api:tasks-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
