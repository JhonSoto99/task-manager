from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.viewsets import TaskViewSet

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

router = DefaultRouter()
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", TaskListView.as_view(), name="list_task"),
    path("add/", TaskCreateView.as_view(), name="add_task"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="edit_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path("", include(router.urls)),
]
