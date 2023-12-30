from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('mail/<int:pk>/', mail_detail, name='detail'),
    path('mail_add/', mail_add, name='mail_add'),
    path('register/', RegistrationFormView.as_view(), name='register'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='users/login.html'),
         name='password_reset_complete'),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset.html',
             html_email_template_name='users/password_reset_email.html'
         ),
         name='password-reset'
         )
]
