from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.viewsets import TaskViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
