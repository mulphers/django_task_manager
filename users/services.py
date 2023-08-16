from tasks.models import Tasks

from datetime import date


def check_overdue_tasks(user):
    overdue_tasks = Tasks.objects.filter(
        user=user,
        created__date__lt=date.today(),
        completed=False,
        check=False
    )

    if overdue_tasks.exists():
        user.number_of_overdue_tasks += len(overdue_tasks)
        user.save()

        for obj in overdue_tasks:
            obj.check = True
            obj.save()


def decrease_counter_of_completed_tasks(user, task):
    if task.completed:
        user.number_of_completed_tasks -= 1
        user.save()
