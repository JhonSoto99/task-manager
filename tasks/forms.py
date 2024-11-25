from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "email", "expiration_date"]
        widgets = {
            "expiration_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }
