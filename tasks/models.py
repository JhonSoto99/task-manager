from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """Model to store tasks."""

    title = models.CharField(max_length=128, help_text="Title of the task.")
    email = models.EmailField("Email associated with the task.")
    description = models.TextField(help_text="Description of the task.")
    expiration_date = models.DateTimeField(
        verbose_name="Expiration date", help_text="Expiration date of the task."
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return f"{self.title}"
