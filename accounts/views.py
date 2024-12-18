import random
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail


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
               # print("Username Taken")
                messages.info(request, "Username Taken")
            elif User.objects.filter(email=email_id).exists():
               # print("Email Taken")
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
          #  print("password doesnt match")
            messages.info(request, "Password Doesn't Match!!")
    return render(request, "accounts/register.html")


def login_user(request):
    if request.user.is_authenticated == True:
        role = request.session['role']
        groups = request.user.groups.values_list("name", flat=True).first()
       # print(role in groups)
       # print(groups)
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
                       # print("hiii")
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


def send_otp_email(request, otp):
    try:
        subject = "The OTP for Password Change"
        username = request.POST.get("username")
        email = request.POST.get("email")
        message = f"Dear {username},\n\nThe OTP for password change is: {otp}.\n\nRegards,\nYour Team"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [request.session['email']]
        send_mail(subject, message, from_email, recipient_list)
        print("Email sent successfully")
        return "Email sent successfully!"
    except Exception as e:
        print(f"Error sending email: {e}")
        return f"Error sending email: {e}"


def generate_otp():
    otp = random.randint(100000, 99999999)
    # print(otp)
    return otp

def forgot_password(request):
    if 'state' not in request.session or request.session['state'] == 'email':
        request.session['state'] = 'email'  
   
    if request.method == "GET":
        if request.session['state'] != 'email':
            request.session['state'] = 'email'
            return redirect('forgot_password')  

    if request.method == "POST":
        if request.session['state'] == 'email':
            request.session['username'] = request.POST.get("username")
            request.session['email'] = request.POST.get("email")
            request.session['role'] = request.POST.get("role")
            try:
                user = User.objects.get(username=request.session['username'])
                if user.email == request.session['email'] and user.groups.filter(name=request.session['role']).exists():
                    request.session['sys_Otp'] = generate_otp()
                    send_otp_email(request, request.session['sys_Otp'])
                    request.session['state'] = 'otp'
                    messages.success(request, "OTP sent to your email.")
                else:
                    messages.error(request, "Incorrect email or role.")
            except User.DoesNotExist:
                messages.error(request, "Invalid Username.")
            except Exception as e:
                messages.error(request, f"Error occurred: {e}")

        elif request.session['state'] == 'otp':
            user_otp = request.POST.get('otp')
            if user_otp == str(request.session.get('sys_Otp')):
                request.session['state'] = 'reset'
                messages.success(request, "OTP verified successfully.")
            else:
                messages.error(request, "Invalid OTP. Please try again.")

        elif request.session['state'] == 'reset':
            username_input = request.POST.get("username")
            new_password = request.POST.get('new_psd')
            confirm_password = request.POST.get('con_new_psd')
            if username_input == request.session.get('username'):
                if new_password == confirm_password:
                    try:
                        user = User.objects.get(username=request.session['username'])
                        user.set_password(new_password)
                        user.save()
                        request.session.flush()
                        messages.success(request, "Password reset successfully!")
                        return redirect('login')  
                    except Exception as e:
                        messages.error(request, f"Error updating password: {e}")
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Username mismatch.")

    return render(request, "accounts/forgot_password.html")

def resend_otp(request):
    if request.method == "POST":
        if request.session.get('state') == 'otp':
            try:
                new_otp = generate_otp()
                request.session['sys_Otp'] = new_otp
                send_otp_email(request, new_otp)
                return JsonResponse({"success": True, "message": "OTP resent successfully."})
            except Exception as e:
                return JsonResponse({"success": False, "message": f"Error: {str(e)}"})
        else:
            return JsonResponse({"success": False, "message": "Invalid state for resending OTP."})
    return JsonResponse({"success": False, "message": "Invalid request method."})