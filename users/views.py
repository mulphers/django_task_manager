from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, PasswordResetConfirmView,
                                       PasswordResetView)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from common.mixins import LogoutRequiredMixin, TitleMixin

from .forms import (ChangePasswordForm, ProfileUpdateForm, SignInForm,
                    SignUpForm)
from .models import Users
from .services import email_confirmation_check


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


class EmailVerifiedView(View):
    @staticmethod
    def get(_request, *_args, **kwargs):
        email_confirmation_check(
            email=kwargs.get('email'),
            code=kwargs.get('code')
        )

        return redirect('/')


class PasswordRecoveryView(TitleMixin, LogoutRequiredMixin, PasswordResetView):
    email_template_name = 'users/email_template.html'
    subject_template_name = 'users/subject_template.txt'
    template_name = 'users/password_recovery.html'
    title = 'DT - Восстановить пароль'
    success_url = reverse_lazy('users:sign_in')
    from_email = settings.EMAIL_HOST_USER


class ChangePasswordView(TitleMixin, LogoutRequiredMixin, PasswordResetConfirmView):
    template_name = 'users/change_password.html'
    title = 'DT - Изменить пароль'
    success_url = reverse_lazy('users:sign_in')
    form_class = ChangePasswordForm
