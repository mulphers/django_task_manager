from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from common.mixins import AffiliationMixin, TitleMixin

from .forms import AddNewTaskForm, EditTaskForm
from .models import Tasks


class IndexView(TitleMixin, TemplateView):
    template_name = 'tasks/index.html'
    title = 'DT - Главная'


class CreateTaskView(TitleMixin, LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = AddNewTaskForm
    success_url = reverse_lazy('tasks:task_list')
    template_name = 'tasks/add-task.html'
    title = 'DT - Добавить задание'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return super().form_valid(form)


class EditTaskView(TitleMixin, LoginRequiredMixin, AffiliationMixin, UpdateView):
    model = Tasks
    form_class = EditTaskForm
    success_url = reverse_lazy('tasks:task_list')
    template_name = 'tasks/edit-task.html'
    title = 'DT - Изменить задание'


class DeleteTaskView(AffiliationMixin, DeleteView):
    model = Tasks
    success_url = reverse_lazy('tasks:task_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TaskListView(TitleMixin, LoginRequiredMixin, ListView):
    template_name = 'tasks/tasks.html'
    title = 'DT - Задания на день'

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
