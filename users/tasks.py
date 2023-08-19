from uuid import uuid4

from celery import shared_task

from .models import EmailVerifications, Users


@shared_task
def send_email_verification(user_id):
    record = EmailVerifications.objects.create(
        code=uuid4(),
        user=Users.objects.get(id=user_id)
    )

    record.send_verification_email()
