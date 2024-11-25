from rest_framework.serializers import ModelSerializer

from tasks.models import Task


class TaskSerializer(ModelSerializer):
    """
    Serializer for Task model.

    Fields:
    - title: The title of the task.
    - description: A brief description of the task.
    - expiration_date: The expiration date of the task.
    - user: The user to whom the task is assigned.
    """

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "email",
            "expiration_date",
            "user",
        ]
