from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
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
                user_group = Group.objects.get(name="SuperAdmin")
                user.groups.add(user_group)
                return redirect("login")
        else:
            print("password doesnt match")
            messages.info(request, "Password Doesn't Match!!")
    return render(request, "accounts/register.html")


