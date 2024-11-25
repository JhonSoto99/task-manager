from django.db.models.signals import post_save
from django.dispatch import receiver

from tasks.models import Task
from tasks.tasks import send_notification_email


@receiver(post_save, sender=Task)
def notify(sender, instance, created, **kwargs):
    """
    Sends an email notification when a task is created or updated.

    Trigger:
        Executed automatically after a Task instance is saved.

    Args:
        sender (Model): The model class that triggered the signal.
        instance (Task): The specific Task instance being saved.
        created (bool): Indicates if a new instance was created (True)
                        or an existing instance was updated (False).
        **kwargs: Additional keyword arguments provided by the signal.
    """
    subject = "Nes task created" if created else "Task updated"
    message = (
        f"Hello {instance.user.username},\n\n"
        f"Title: {instance.title}\n"
        f"Description: {instance.description}\n"
        f"Expiraton date: {instance.expiration_date}\n\n"
    )
    recipient_email = instance.email
    send_notification_email.delay(subject, message, recipient_email)
