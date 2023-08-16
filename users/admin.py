from django.contrib import admin

from tasks.models import Tasks
from users.models import EmailVerifications, Users


class TasksInLine(admin.StackedInline):
    model = Tasks
    fields = ('task', 'short_description', 'stage', 'created', 'completed')
    readonly_fields = ('created',)
    extra = 0


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'last_login',)
    list_display_links = ('id', 'username',)
    fields = ('username',
              ('first_name', 'last_name'),
              ('email', 'email_verified'),
              ('date_joined', 'last_login'),
              ('is_superuser', 'is_staff'),
              ('number_of_completed_tasks', 'number_of_overdue_tasks'),
              )
    search_fields = ('username',)
    inlines = (TasksInLine,)

    def get_form(self, request, obj=None, change=False, **kwargs):
        """
        Изменение отображаемого имя поля для:
        1. number_of_completed_tasks -> Количество выполненных задач
        2. number_of_overdue_tasks -> Количество просроченных задач
        """

        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        form.base_fields['number_of_completed_tasks'].label = 'Количество выполненных задач'
        form.base_fields['number_of_overdue_tasks'].label = 'Количество просроченных задач'

        return form


@admin.register(EmailVerifications)
class EmailVerificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created',)
