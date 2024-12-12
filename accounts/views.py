from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email_id = request.POST.get("email_id")
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        conf_passwd = request.POST.get("conf_passwd")
        if passwd == conf_passwd:
            if User.objects.filter(username=username).exists():
                print("Username Taken")
                messages.info(request, "Username Taken")
            elif User.objects.filter(email=email_id).exists():
                print("Email Taken")
                messages.info(request, "Email Taken")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=passwd,
                    email=email_id,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                user_group = Group.objects.get(name="InstituteAdmin")
                user.groups.add(user_group)
                return redirect("login")
        else:
            print("password doesnt match")
            messages.info(request, "Password Doesn't Match!!")
    return render(request, "accounts/register.html")


def login_user(request):
    if request.user.is_authenticated == True:
        role = request.session['role']
        groups = request.user.groups.values_list("name", flat=True).first()
        print(groups)
        if role in groups and role == "InstituteAdmin":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "Chancellor":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "ViceChancellor":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "Principal":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "AttendanceAdmin":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "ExamAdmin":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "HeadOfDepartment":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "DeputyHeadOfDepartment":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "Teacher":
            return redirect("teacher_dashboard")
        elif role in groups and role == "Student":
            return redirect("student_dashboard")
        elif role in groups and role == "Parent":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "Assistant":
            return redirect("super_admin_dashboard")
        elif role in groups and role == "Staff":
            return redirect("super_admin_dashboard")
    else:
        try:
            if request.method == "POST":
                username = request.POST.get("username")
                passwd = request.POST.get("passwd")
                role = request.POST.get("role")
                logging_user = authenticate(username=username, password=passwd)
                if logging_user is not None:
                    logging_user_instance = User.objects.get(username=username)
                    last_login_value = logging_user_instance.last_login
                    if last_login_value != None:
                        login(request, logging_user)
                        print("hi", last_login_value)
                        request.session['role'] = role
                        groups = request.user.groups.values_list(
                            "name", flat=True)
                        print(groups)
                        if role in groups and role == "InstituteAdmin":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "Chancellor":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "ViceChancellor":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "Principal":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "AttendanceAdmin":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "ExamAdmin":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "HeadOfDepartment":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "DeputyHeadOfDepartment":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "Teacher":
                            return redirect("teacher_dashboard")
                        elif role in groups and role == "Student":
                            return redirect("student_dashboard")
                        elif role in groups and role == "Parent":
                            return redirect("super_admin_dashboard")
                        elif role in groups and role == "Assistant":
                            return redirect("super_admin_dashboard")
                    else:
                        print("hiii")
                        return redirect("first_login_reset_password")
                        # return redirect("super_admin_dashboard")
                else:
                    messages.info(request, "Invalid Username / Password")
            else:
                return render(request, "accounts/login.html")

        except Exception as e:
            print(e)

    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")

def first_login_reset_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        current_passwd = request.POST.get("current_passwd")
        new_passwd = request.POST.get("new_passwd")
        conf_new_passwd = request.POST.get("conf_new_passwd")
        role = request.POST.get("role")
        if new_passwd == conf_new_passwd:
            logging_user = authenticate(username=username, password=current_passwd)
            if logging_user is not None:
                user_first_login = User.objects.get(username=username)
                user_first_login.set_password(new_passwd)
                user_first_login.save()
                login(request, logging_user)
                groups = request.user.groups.values_list(
                            "name", flat=True)
                print(groups)
                if role in groups and role == "InstituteAdmin":
                    return redirect("institute_admin_dashboard")
                elif role in groups and role == "Chancellor":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "ViceChancellor":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "Principal":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "AttendanceAdmin":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "ExamAdmin":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "HeadOfDepartment":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "DeputyHeadOfDepartment":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "Teacher":
                    return redirect("teacher_dashboard")
                elif role in groups and role == "Student":
                    return redirect("student_dashboard")
                elif role in groups and role == "Parent":
                    return redirect("super_admin_dashboard")
                elif role in groups and role == "Assistant":
                    return redirect("super_admin_dashboard")
            else:
                messages.info(request, "Username / Password is incorrect")
        else:
            messages.info(request, "New Password and Confirm Password Doesn't Match!!")

    return render(request, "accounts/first_login_reset_password.html")
