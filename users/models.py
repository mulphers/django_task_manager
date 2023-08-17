from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse_lazy


class Users(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    number_of_completed_tasks = models.PositiveIntegerField(default=0)
    number_of_overdue_tasks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Пользователь {self.username}'

    def get_completion_percentage(self, for_completed=True):
        value = self.number_of_completed_tasks if for_completed else self.number_of_overdue_tasks

        if not value:
            return 0

        coefficient = sum((self.number_of_completed_tasks,
                           self.number_of_overdue_tasks)) / value

        return int(100 / coefficient)

    def get_overdue_percentage(self):
        return self.get_completion_percentage(for_completed=False)


class EmailVerifications(models.Model):
    code = models.UUIDField(unique=True)
    user = models.OneToOneField(to=Users, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подтверждение электронной почты'
        verbose_name_plural = 'Подтверждение электронных почт'

    def __str__(self):
        return f'Подтверждение для пользователя {self.user.username}'

    def send_verification_email(self):
        link = reverse_lazy('users:verify', kwargs={
            'email': self.user.email,
            'code': self.code
        })
        verification_link = f'{settings.DOMAIN_NAME}{link}'

        subject = 'Daily Tasks - Подтверждение адреса электронной почты'
        message = 'Спасибо за регистрацию!\n\nДля подтверждения адреса электронной' \
                  ' почты перейдите по ссылке:\n {}'.format(verification_link)

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )
