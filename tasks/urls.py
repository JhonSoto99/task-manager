from django.urls import path
from rest_framework.routers import DefaultRouter

from tasks.api.viewsets import TaskViewSet

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

router = DefaultRouter()
router.register("tasks", TaskViewSet)

app_name = "web"

urlpatterns = [
    path("", TaskListView.as_view(), name="list_task_web"),
    path("add/", TaskCreateView.as_view(), name="add_task_web"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="edit_task_web"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task_web"),
]
