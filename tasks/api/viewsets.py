from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import viewsets

from tasks.api.serializers import TaskSerializer
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(
        summary="Retrieve a list of tasks",
        description="This endpoint returns a list of all tasks.",
        responses={200: TaskSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        """
        Retrieve all tasks.
        """
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new task",
        description="This endpoint creates a new task and returns the created task.",
        request=TaskSerializer,
        responses={201: TaskSerializer},
    )
    def create(self, request, *args, **kwargs):
        """
        Create a new task.
        """
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Retrieve a task by ID",
        description="This endpoint retrieves a specific task based on the provided ID.",
        responses={
            200: TaskSerializer,
            404: OpenApiResponse(description="Task not found"),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a task by ID.
        """
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Update an existing task",
        description="This endpoint updates an existing task based on the provided ID.",
        request=TaskSerializer,
        responses={
            200: TaskSerializer,
            404: OpenApiResponse(description="Task not found"),
        },
    )
    def update(self, request, *args, **kwargs):
        """
        Update an existing task.
        """
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update an existing task",
        description="This endpoint partially updates an existing task based on the provided ID. Only the fields passed will be updated.",
        request=TaskSerializer,
        responses={
            200: TaskSerializer,
            404: OpenApiResponse(description="Task not found"),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an existing task.
        """
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a task",
        description="This endpoint deletes the specified task based on the provided ID.",
        responses={
            204: OpenApiResponse(description="Task deleted successfully"),
            404: OpenApiResponse(description="Task not found"),
        },
    )
    def destroy(self, request, *args, **kwargs):
        """
        Delete a task.
        """
        return super().destroy(request, *args, **kwargs)
