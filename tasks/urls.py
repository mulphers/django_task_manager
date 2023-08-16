from django.urls import path

from .views import CreateTaskView, DeleteTaskView, EditTaskView, TaskListView

app_name = 'tasks'

urlpatterns = [
    path('task-list/', TaskListView.as_view(), name='task_list'),
    path('add-task/', CreateTaskView.as_view(), name='add_task'),
    path('edit-task/<int:pk>', EditTaskView.as_view(), name='edit_task'),
    path('delete-task/<int:pk>', DeleteTaskView.as_view(), name='delete_task')
]
