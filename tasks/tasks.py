from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_notification_email(subject, message, recipient_email):
    """
    Sends an asynchronous email notification.

    Args:
        subject (str): Email subject.
        message (str): Email body content.
        recipient_email (str): Recipient's email address.
    """
    send_mail(
        subject,
        message,
        "no-reply@example.com",
        [recipient_email],
        fail_silently=False,
    )
