from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from accounts import constants, decorators
from universities.forms import manageUniversityForm, manageSelectUniversityForm
from universities.models import University_Details, user_university
from django.db.models import Q
from django.contrib import messages

# Create your views here.


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_university_ins_fn(request):
    if request.method == "POST":
        university_check = user_university.objects.filter(
            user=request.user).values('user', 'university')
        print(university_check)
        if university_check.exists() == False:
            print("User is entering the university for the first time.")
            manage_university_form = manageUniversityForm(request.POST)
            if manage_university_form.is_valid():
                manage_university_save = manage_university_form.save(
                    commit=False)
                manage_university_save.created_by = request.user
                manage_university_save.updated_by = request.user
                manage_university_save.save()
                
                university_created = University_Details.objects.filter(
                    Q(created_by=1) | Q(created_by=request.user)
                ).order_by("-id")[0]
                print(university_created)
                user_university_row = user_university(
                    user=request.user, university=university_created
                )
                user_university_row.save()
                messages.success(request,'University added successfully')
                return redirect("manage_university_ins")
            else:
                for field_name, errors in manage_university_form.errors.items():
                    for error_message in errors:
                        print(error_message)
                        messages.error(request, f"{error_message}")
                return redirect("manage_university_ins")
                
        else:
            print("User has already entered this university.")
            messages.error(request, 'User has already entered this university')
            university_id = university_check.values("university")[
                0]["university"]
            return redirect("manage_university_upd", university_id=university_id)

    manage_university_form = manageUniversityForm()
    manage_university_table_data = University_Details.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )
    university_created_flag = ""
    if University_Details.objects.filter(created_by=request.user).exists():
        university_created_flag = "true"
    else:
        university_created_flag = "false"
    print(university_created_flag)
    data = {
        "university_created_flag": university_created_flag,
        "manage_university_form": manage_university_form,
        "manage_university_table_data": manage_university_table_data,
    }
    return render(request, "universities/manage_universities.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_university_upd_fn(request, university_id):
    university_inst = University_Details.objects.get(id=university_id)
    manage_university_form = manageUniversityForm(instance=university_inst)
    if request.method == "POST":
        manage_university_form = manageUniversityForm(
            request.POST, instance=university_inst
        )
        if manage_university_form.is_valid():
            manage_university_save = manage_university_form.save(commit=False)
            manage_university_save.updated_by = request.user
            manage_university_save.save()
            messages.success(request,'Details updated successfully')
            return redirect("manage_university_ins")
        else:
            for field_name, errors in manage_university_form.errors.items():
                for error_message in errors:
                    print(error_message)
                    messages.error(request, f"{error_message}")
            return redirect("manage_university_ins")

    manage_university_table_data = University_Details.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )
    print(manage_university_table_data)
    data = {
        "manage_university_form": manage_university_form,
        "manage_university_table_data": manage_university_table_data,
    }
    return render(request, "universities/manage_universities.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_university_del_fn(request, uni_id):
    university_inst = University_Details.objects.get(id=uni_id)
    university_inst.delete()
    user_university_inst = user_university.objects.get(user=request.user)
    user_university_inst.delete()
    messages.success(request,'University deleted successfully!')
    return redirect("manage_university_ins")


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_university_sel_fn(request):
    if request.method == "POST":
        university_check = user_university.objects.filter(
            user=request.user).values()
        manage_select_university_form = manageSelectUniversityForm(
            request.POST)
        if manage_select_university_form.is_valid():
            selected_university = manage_select_university_form.cleaned_data[
                "university"
            ]
            print(selected_university)
            if university_check.exists() == False:
                manage_select_university_save = manage_select_university_form.save(
                    commit=False
                )
                manage_select_university_save.user = request.user
                manage_select_university_save.save()
                return redirect("manage_university_sel")
            else:
                user_university_row = user_university.objects.get(
                    user=request.user)
                user_university_row.university = selected_university
                user_university_row.save()
        else:
            print(manage_select_university_form.errors)
    manage_select_university_form = manageSelectUniversityForm()
    university_list = (
        University_Details.objects.filter(
            Q(created_by=1) | Q(created_by=request.user))
        .values()
        .distinct()
    )
    manage_select_university_form.fields["university"].choices = []
    manage_select_university_form.fields["university"].choices.insert(
        0, ("", "Select")
    )

    for university in university_list:
        print(university.get("id"), university.get("university_name"))
        id = university.get("id")
        university_name = university.get("university_name")
        manage_select_university_form.fields["university"].choices.append(
            (id, university_name)
        )
    selected_university = ""
    if user_university.objects.filter(user=request.user).exists():
        selected_university = user_university.objects.get(
            user=request.user).university
    else:
        selected_university = "false"
    data = {
        "manage_select_university_form": manage_select_university_form,
        "selected_university": selected_university,
    }
    return render(request, "universities/select_university.html", data)
