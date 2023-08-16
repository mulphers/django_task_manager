from django.db import models

from users.models import Users


class Tasks(models.Model):
    EXPECTATION = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    STAGE_CHOICE = (
        (EXPECTATION, 'Ожидание'),
        (IN_PROGRESS, 'В процессе'),
        (COMPLETED, 'Выполнено'),
    )

    task = models.CharField(max_length=32)
    short_description = models.TextField(max_length=128)
    stage = models.PositiveSmallIntegerField(default=EXPECTATION, choices=STAGE_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    check = models.BooleanField(default=False)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'Задание пользователя {self.user.username}'
