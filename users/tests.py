from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy

from .models import Users


class SignUpViewTestCases(TestCase):
    def setUp(self):
        self.path = reverse_lazy('users:sign_up')
        self.data = {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'username': 'test_username',
            'email': 'test_email@gmail.com',
            'password1': '1234567pP',
            'password2': '1234567pP'
        }

    def test_sign_up_get(self):
        response = self.client.get(
            path=self.path
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/sign-up.html')
        self.assertEqual(response.context_data.get('title'), 'DT - Регистрация')

    def test_sign_up_post_error(self):
        Users.objects.create(username=self.data.get('username'))

        response = self.client.post(
            path=self.path,
            data=self.data
        )

        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)


class SignInViewTestCases(TestCase):
    def setUp(self):
        self.path = reverse_lazy('users:sign_in')
        self.data = {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'username': 'test_username',
            'email': 'test_email@gmail.com',
            'password': '1234567pP',
        }

    def test_sign_in_get(self):
        response = self.client.get(
            path=self.path
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/sign-in.html')
        self.assertEqual(response.context_data.get('title'), 'DT - Авторизация')

    def test_sign_in_post_error(self):
        Users.objects.create(**self.data)

        response = self.client.post(
            path=self.path,
            data={
                'username': self.data.get('username'),
                'password': '...'
            }
        )

        self.assertContains(response, 'Пожалуйста, введите правильные имя пользователя и пароль.'
                                      ' Оба поля могут быть чувствительны к регистру.', html=True)


class ProfileViewTestCases(TestCase):
    def setUp(self):
        self.path = reverse_lazy('users:profile', kwargs={'pk': 1})

    def test_profile_get_without_sign_in(self):
        response = self.client.get(
            path=self.path
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
