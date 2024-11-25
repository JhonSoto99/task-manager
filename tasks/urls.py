from django.urls import path

from .views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="list_task"),
    path("add/", TaskCreateView.as_view(), name="add_task"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="edit_task"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete_task"),
]
