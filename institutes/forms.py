from django.core import validators
from django import forms
from .models import Institute_Details, Institute_type, Registration_Authority, Institute_Registration_Authority, Institute_Inst_type


class manageInstituteTypeForm(forms.ModelForm):
    class Meta:
        model = Institute_type
        fields = ["inst_type_name"]
        labels = {
            "inst_type_name": "Institute type Name",
        }
        help_text = {
            "inst_type_name": "Enter the Institute type Name",
        }
        error_messages = {
            "inst_type_name": {"required": "Enter the Institute type Name"},
        }
        widgets = {
            "inst_type_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institite type Name",
                }
            )
        }


class manageInstituteForm(forms.ModelForm):
    class Meta:
        model = Institute_Details
        fields = ["inst_name", "inst_address", "inst_pincode", "uni_id"]
        labels = {
            "inst_name": "Institute Name",
            "inst_address": "Institute Address",
            "inst_pincode": "Institute Pin code",
            "uni_id": "University id",

        }
        help_text = {
            "inst_name": "Enter the Institute Name",
            "inst_address": "Enter Institute Address",
            "inst_pincode": "Enter the pin code",
            "uni_id": "Enter University id",
        }
        error_messages = {
            "inst_name": {"required": "Enter the University Name"},
            "inst_address": {"required": "Enter Date of Establishment"},
            "inst_pincode": {"required": "Enter the university description"},
            "uni_id": {"required": "Enter Chancellor"},

        }
        widgets = {
            "inst_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute Name",
                }
            ),
            "inst_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute Address",
                }
            ),
            "inst_pincode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Pin code",
                }
            ),
            "uni_id": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Univeristy",
                }
            ),

        }
    def clean(self):
        cleaned_data = super().clean()
        inst_name = cleaned_data.get('inst_name')
        inst_address = cleaned_data.get('inst_address')
        inst_pincode = cleaned_data.get('inst_pincode')

        # Add your custom validation logic here

        if inst_name:
            if len(inst_name) < 3:
                self.add_error('inst_name', 'Institute Name must be at least 3 characters long.')

        if inst_address:
            if len(inst_address) > 100:
                self.add_error('inst_address', 'Institute Address cannot exceed 100 characters.')

        if inst_pincode:
            if not inst_pincode.isdigit() or len(inst_pincode) != 6:
                self.add_error('inst_pincode', 'Pin code should contain 6 numerical characters.')

        return cleaned_data


class manageRegistrationAuthorityForm(forms.ModelForm):
    class Meta:
        model = Registration_Authority
        fields = ["ra_name"]
        labels = {
            "ra_name": "Registration Authority Name",

        }
        help_text = {
            "ra_name": "Enter the Registration Authority Name",
        }
        error_messages = {
            "ra_name": {"required": "Enter the Registration Authority Name"},
        }
        widgets = {
            "ra_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Registration Authority Name",
                }
            )
        }


class manageInstRAForm(forms.ModelForm):
    class Meta:
        model = Institute_Registration_Authority
        fields = ["inst_id", "ra_id", "reg_date", "code", "end_date"]
        labels = {
            "inst_id": "Institite ID",
            "ra_id": "Registration Authority ID",
            "reg_date": "Registration date (mm/dd/yyyy)",
            "code": "Registration code",
            "end_date": "Registration end date",

        }
        help_text = {
            "inst_id": "Enter the Institite ID",
            "ra_id": "Enter the Registration Authority ID",
            "reg_date": "Enter the Registration date (mm/dd/yyyy)",
            "code": "Enter the Registration code",
            "end_date": "Enter the Registration end date",
        }
        error_messages = {
            "inst_id": {"required": "Enter the Institite ID"},
            "ra_id": {"required": "Enter the Registration Authority ID"},
            "reg_date": {"required": "Enter the Registration date (mm/dd/yyyy)"},
            "code": {"required": "Enter the Registration code"},
            "end_date": {"required": "Enter the Registration end date"},
        }
        widgets = {
            "inst_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institite ID",
                }
            ),
            "ra_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Registration Authority ID",
                }
            ),
            "reg_date": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Registration date",
                }
            ),
            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Registration code",
                }
            ),
            "end_date": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Registration end date",
                }
            )
        }


class manageInstituteInstTypeForm(forms.ModelForm):
    class Meta:
        model = Institute_Inst_type
        fields = ["inst_type_id"]
        labels = {
            "inst_type_id": "Institute Type ID"
        }
        help_text = {
            "inst_type_id": "Enter the Institute Type ID"
        }
        error_messages = {
            "inst_type_id": {"required": "Enter the Institute Type ID"},
        }
        widgets = {
            "inst_type_id": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Institute Type ID",
                }
            )
        }
