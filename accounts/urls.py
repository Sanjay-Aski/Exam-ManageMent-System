from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("register", views.register_user, name="register"),
    path("logout", views.logout_user, name="logout"),
    path("resend-otp", views.resend_otp, name="resend_otp"),
    path("first-login-reset-password", views.first_login_reset_password, name="first_login_reset_password"),
    path("forgot-password",views.forgot_password , name = "forgot_password")
]
