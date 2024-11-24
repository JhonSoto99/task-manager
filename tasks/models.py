from django.db import models


class Task(models.Model):
    """Model to store tasks."""
    title = models.CharField(max_length=128, help_text="Title of the task.")
    email = models.EmailField("Email associated with the task.")
    description = models.TextField(help_text="Description of the task.")
    expiration_date = models.DateTimeField(help_text="Expiration date of the task.")

    def __str__(self):
        return f"{self.title}"