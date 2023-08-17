from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import EmailVerifiedView, ProfileView, SignInView, SignUpView

app_name = 'users'

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-out/', LogoutView.as_view(), name='sign_out'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('email-verified/<str:email>/<uuid:code>', EmailVerifiedView.as_view(), name='verify')
]
