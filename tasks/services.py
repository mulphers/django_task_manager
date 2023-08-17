from datetime import date

from .models import Tasks


def check_overdue_tasks(user):
    overdue_tasks = Tasks.objects.filter(
        user=user,
        created__date__lt=date.today(),
        completed=False,
    )

    if overdue_tasks.exists():
        user.number_of_overdue_tasks += len(overdue_tasks)
        user.save()

        overdue_tasks.delete()


def increase_counter_of_completed_tasks(stage, user, task):
    if stage == 2:
        task.completed = True
        task.save()

        user.number_of_completed_tasks += 1
        user.save()


def decrease_counter_of_completed_tasks(user, task):
    if task.completed:
        user.number_of_completed_tasks -= 1
        user.save()
