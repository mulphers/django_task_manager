from django.core.exceptions import ObjectDoesNotExist

from .models import EmailVerifications, Users


def email_confirmation_check(email, code):
    try:
        user = Users.objects.get(email=email)
        email_verification = EmailVerifications.objects.filter(user=user, code=code)

        if email_verification.exists():
            user.email_verified = True
            user.save()

    except ObjectDoesNotExist:
        pass
