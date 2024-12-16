from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts import decorators, constants


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def institute_admin_dashboard(request):
    print("H")
    return render(request, "dashboards/instituteadmin/instituteadmin_dashboard.html")


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.Teacher)
def teacher_dashboard(request):
    print("hello")
    return render(request, "dashboards/teacher/teacher_dashboard.html")


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.Student)
def student_dashboard(request):
    return render(request, "dashboards/student/student_dashboard.html")


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.Assistant)
def assistant_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")
