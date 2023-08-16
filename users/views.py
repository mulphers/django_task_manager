from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from common.mixins import LogoutRequiredMixin, TitleMixin

from .forms import ProfileUpdateForm, SignInForm, SignUpForm
from .models import Users


class SignInView(TitleMixin, LogoutRequiredMixin, LoginView):
    template_name = 'users/sign-in.html'
    title = 'DT - Авторизация'
    form_class = SignInForm

    def get_success_url(self):
        return reverse_lazy('user:profile', kwargs={'pk': self.request.user.id})


class SignUpView(TitleMixin, LogoutRequiredMixin, CreateView):
    model = Users
    form_class = SignUpForm
    template_name = 'users/sign-up.html'
    title = 'DT - Регистрация'
    success_url = reverse_lazy('user:sign_in')


class ProfileView(TitleMixin, LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    title = 'DT - Профиль'
    model = Users
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
