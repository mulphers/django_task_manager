from uuid import uuid4

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .models import EmailVerifications, Users


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = Users
        fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Электронная почта'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def get_errors_values(self):
        return (error for error in self.errors.values())

    def save(self, commit=True):
        user = super().save(commit=commit)

        record = EmailVerifications.objects.create(
            code=uuid4(),
            user=user
        )

        record.send_verification_email()

        return user


class ProfileUpdateForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'id': 'avatar',
        'class': 'btn btn-primary',
        'size': '50'
    }), required=False)

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'image')
