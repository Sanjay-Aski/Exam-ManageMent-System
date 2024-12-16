from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts import constants, decorators
from institutes.forms import manageInstituteTypeForm, manageInstituteForm, manageInstituteInstTypeForm, manageInstRAForm, manageRegistrationAuthorityForm
from institutes.models import Institute_type, Institute_Details, Institute_Inst_type
from django.db.models import Q
from django.contrib import messages

# Create your views here.

'''
@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_type_ins_fn(request):
    if request.method == "POST":
        manage_inst_type_form = manageInstituteTypeForm(request.POST)
        if manage_inst_type_form.is_valid():
            manage_inst_type_save = manage_inst_type_form.save(commit=False)
            manage_inst_type_save.created_by = request.user
            manage_inst_type_save.updated_by = request.user
            manage_inst_type_save.save()
            messages.success(request, "Added Institute type successfully!")
            return redirect("manage_inst_type_ins")
        else:
            print(manage_inst_type_form.errors)
            for field_name, errors in manage_inst_type_form.errors.items():
                for error_message in errors:
                    print(error_message)
                    messages.error(request, f"{error_message}")
            return redirect("manage_inst_type_ins")
    manage_inst_type_form = manageInstituteTypeForm()
    manage_inst_type_table_data = Institute_type.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )
    data = {
        "manage_inst_type_form": manage_inst_type_form,
        "manage_inst_type_table_data": manage_inst_type_table_data,
    }
    return render(request, "institutes/manage_inst_type.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_type_upd_fn(request, inst_type_id):
    inst_type_inst = Institute_type.objects.get(id=inst_type_id)
    manage_inst_type_form = manageInstituteTypeForm(instance=inst_type_inst)
    if request.method == "POST":
        manage_inst_type_form = manageInstituteTypeForm(
            request.POST, instance=inst_type_inst
        )
        if manage_inst_type_form.is_valid():
            manage_inst_type_save = manage_inst_type_form.save(commit=False)
            manage_inst_type_save.updated_by = request.user
            manage_inst_type_save.save()
            messages.success(request, "Updated Institute type successfully!")
            return redirect("manage_inst_type_ins")
        else:
            for field_name, errors in manage_inst_type_form.errors.items():
                for error_message in errors:
                    print(error_message)
                    messages.error(request, f"{error_message}")
            return redirect("manage_inst_type_ins")
    manage_inst_type_table_data = Institute_type.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )
    print(manage_inst_type_table_data)
    data = {
        "manage_inst_type_form": manage_inst_type_form,
        "manage_inst_type_table_data": manage_inst_type_table_data,
    }
    return render(request, "institutes/manage_inst_type.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_type_del_fn(request, inst_type_id):
    inst_type_inst = Institute_type.objects.get(id=inst_type_id)
    inst_type_inst.delete()
    return redirect("manage_inst_type_ins")
'''
# manage institute detail

@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_with_inst_type_ins_fn(request):
    if request.method == "POST":
        manage_inst_with_inst_type_form = manageInstituteInstTypeForm(request.POST)
        inst_type_id_value = ""
        inst = Institute_Details.objects.filter(created_by=request.user).first()
        
        if manage_inst_with_inst_type_form.is_valid():
            inst_type_id_value = manage_inst_with_inst_type_form.cleaned_data['inst_type_id']
        institute_inst_type_queryset = Institute_Inst_type.objects.filter(
            inst_id=inst,
            inst_type_id=inst_type_id_value
        )
        
        if institute_inst_type_queryset.exists():
            print("Already Exists")
            return redirect("manage_inst_with_inst_type_ins_fn")
        else:
            if manage_inst_with_inst_type_form.is_valid():
                manage_inst_with_inst_type_save = manage_inst_with_inst_type_form.save(commit=False)
                manage_inst_with_inst_type_save.inst_id = inst
                manage_inst_with_inst_type_save.created_by = request.user
                manage_inst_with_inst_type_save.updated_by = request.user
                manage_inst_with_inst_type_save.save()
                messages.success(request, 'Institute Type Saved successfully')
                return redirect("manage_inst_with_inst_type_ins_fn")
            else:
                print(manage_inst_with_inst_type_form.errors)
                for error_messages in manage_inst_with_inst_type_form.errors.values():
                    for error_message in error_messages:
                        messages.error(request, error_message)
                return redirect("manage_inst_with_inst_type_ins_fn")
            
    manage_inst_with_inst_type_form = manageInstituteInstTypeForm()
    manage_inst_with_inst_type_table_data = Institute_Inst_type.objects.filter(Q(created_by=request.user))
    print(manage_inst_with_inst_type_table_data)
    data = {
        "manage_inst_with_inst_type_form": manage_inst_with_inst_type_form,
        "manage_inst_with_inst_type_table_data": manage_inst_with_inst_type_table_data,
    }
    return render(request, "institutes/manage_inst_with_inst_type.html", data)

@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_with_inst_type_del_fn(request, inst_with_inst_type_id):
    inst_with_inst_type_inst = Institute_Inst_type.objects.get(id=inst_with_inst_type_id)
    inst_with_inst_type_inst.delete()
    return redirect("manage_inst_with_inst_type_ins_fn")


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_ins_fn(request):
    if request.method == "POST":
        manage_inst_form = manageInstituteForm(request.POST)
        if manage_inst_form.is_valid():
            manage_inst_save = manage_inst_form.save(commit=False)
            manage_inst_save.created_by = request.user
            manage_inst_save.updated_by = request.user
            manage_inst_save.save()
            messages.success(request, 'Institute added successfully')
            return redirect("manage_inst_ins")
        else:
            print(manage_inst_form.errors)
            for error_messages in manage_inst_form.errors.values():
                for error_message in error_messages:
                    messages.error(request, error_message)
            return redirect("manage_inst_ins")

    manage_inst_form = manageInstituteForm()
    manage_inst_table_data = Institute_Details.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )
    institute_created_flag = ""
    if Institute_Details.objects.filter(created_by=request.user).exists():
        institute_created_flag = "true"
    else:
        institute_created_flag = "false"
    print("Hello",institute_created_flag)
    data = {
        "institute_created_flag": institute_created_flag,
        "manage_inst_form": manage_inst_form,
        "manage_inst_table_data": manage_inst_table_data,
    }
    return render(request, "institutes/manage_institute.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_upd_fn(request, inst_id):
    institute_inst = Institute_Details.objects.get(id=inst_id)
    manage_inst_form = manageInstituteForm(instance=institute_inst)
    if request.method == "POST":
        manage_inst_form = manageInstituteForm(
            request.POST, instance=institute_inst
        )
        if manage_inst_form.is_valid():
            manage_inst_save = manage_inst_form.save(commit=False)
            manage_inst_save.updated_by = request.user
            manage_inst_save.save()
            messages.success(request, "Updated Institute successfully!")
            return redirect("manage_inst_ins")
        else:
            for field_name, errors in manage_inst_form.errors.items():
                for error_message in errors:
                    print(error_message)
                    messages.error(request, f"{error_message}")
            return redirect("manage_inst_ins")
    manage_inst_table_data = Institute_Details.objects.filter(
        Q(created_by=1) | Q(created_by=request.user)
    )

    institute_created_flag = ""
    if Institute_Details.objects.filter(created_by=request.user).exists():
        institute_created_flag = "true"
    else:
        institute_created_flag = "false"
    print("Hello",institute_created_flag)
    print(manage_inst_table_data)
    data = {
        "institute_created_flag": institute_created_flag,
        "manage_inst_form": manage_inst_form,
        "manage_inst_table_data": manage_inst_table_data,
    }
    return render(request, "institutes/manage_institute.html", data)


@login_required(login_url="login")
@decorators.check_user_able_to_see_page(constants.Group.InstituteAdmin)
def manage_inst_del_fn(request, inst_id):
    institute_inst = Institute_Details.objects.get(id=inst_id)
    institute_inst.delete()
    return redirect("manage_inst_ins")
