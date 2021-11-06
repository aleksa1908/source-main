from django.contrib.auth import views as auth_views
from django.urls import path
from user.views import (
    RegisterUserView,
    LoginView,
    LogoutView,
    ProfileView,
    PasswordChangeView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<str:pk>/profile/', ProfileView.as_view(), name='profile'),

    path("<str:pk>/profile/change_password/",
         auth_views.PasswordResetView.as_view(template_name="user/password_reset.html",
                                              email_template_name='user/password_reset_email.html'),
         name="reset_password"),
    path("reset_password_sent/",
         auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("reset_password_complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),
         name="password_reset_complete")
]
