from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from tasks.models import Tasks


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title

        return context


class LogoutRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect(f'/user/profile/{self.request.user.id}')


class AffiliationMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            return Tasks.objects.get(id=self.kwargs.get('pk')).user == self.request.user
        except ObjectDoesNotExist:
            return False

    def handle_no_permission(self):
        return redirect('/tasks/task-list')


class UserCheckMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            return self.request.user.id == self.kwargs.get('pk')
        except ObjectDoesNotExist:
            return False

    def handle_no_permission(self):
        return redirect(f'/user/profile/{self.request.user.id}')
