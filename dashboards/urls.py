from django.contrib import admin
from django.urls import path
from dashboards import views

urlpatterns = [
    path("institute-admin-dashboard", views.institute_admin_dashboard, name="institute_admin_dashboard"),
    path("teacher-dashboard", views.teacher_dashboard, name="teacher_dashboard"),
    path("student-dashboard", views.student_dashboard, name="student_dashboard"),
    path("assistant-dashboard", views.assistant_dashboard, name="assistant_dashboard"),
]
