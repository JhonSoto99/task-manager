# Generated by Django 5.1.3 on 2024-11-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the task.", max_length=128
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        verbose_name="Email associated with the task.",
                    ),
                ),
                (
                    "description",
                    models.TextField(help_text="Description of the task."),
                ),
                (
                    "expiration_date",
                    models.DateTimeField(
                        help_text="Expiration date of the task."
                    ),
                ),
            ],
        ),
    ]
