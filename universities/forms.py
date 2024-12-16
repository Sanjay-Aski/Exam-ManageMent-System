from django.core import validators
from django import forms
from .models import University_Details,user_university


class manageUniversityForm(forms.ModelForm):
    class Meta:
        model = University_Details
        fields = ["university_name", "Est_Date", "University_Description","Vice_Chancellor","Chancellor"]
        labels = {
            "university_name": "University Name",
            "Est_Date": "Established Date",
            "University_Description": "University Description",
            "Vice_Chancellor":"Vice Chancellor",
            "Chancellor":"Chancellor",

        }
        help_text = {
            "university_name": "Enter the University Name",
            "Est_Date": "Enter Date of Establishment",
            "University_Description":"Enter the university description",
            "Vice_Chancellor":"Enter Vice Chancellor",
            "Chancellor":"Enter Chancellor",
        }
        error_messages = {
            "university_name": {"required": "Enter the University Name"},
            "Est_Date": {"required": "Enter Date of Establishment"},
            "University_Description":{"required": "Enter the university description"},
            "Vice_Chancellor": {"required": "Enter Vice Chancellor"},
            "Chancellor": {"required": "Enter Chancellor"},

        }
        widgets = {
            "university_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "University Name",
                }
            ),
            "Est_Date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Year of Establishment",
                }
            ),
            "University_Description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "University Description",
                }
            ),
            "Vice_Chancellor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Vice_Chancellor",
                }
            ),
            "Chancellor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; margin-bottom: 20px;",
                    "placeholder": "Chancellor",
                }
            ),

        }
    def clean(self):
        cleaned_data = super().clean()
        university_name = cleaned_data.get('university_name')
        Est_Date = cleaned_data.get('Est_Date')
        University_Description = cleaned_data.get('University_Description')
        Vice_Chancellor = cleaned_data.get('Vice_Chancellor')
        Chancellor = cleaned_data.get('Chancellor')


        if university_name:
            if len(university_name) < 3:
                self.add_error('university_name', 'University Name must be at least 3 characters long and contain only alphabetic characters.')

        # Add custom validation for Est_Date (date format) here.

        if University_Description:
            if len(University_Description) > 200:
                self.add_error('University_Description', 'University Description must be a maximum of 200 characters.')

        if Vice_Chancellor:
            if len(Vice_Chancellor) < 3:
                self.add_error('Vice_Chancellor', 'Vice Chancellor must be at least 3 characters long and contain only alphabetic characters.')

        if Chancellor:
            if len(Chancellor) < 3:
                self.add_error('Chancellor', 'Chancellor must be at least 3 characters long and contain only alphabetic characters.')

        return cleaned_data 



class manageSelectUniversityForm(forms.ModelForm):
    class Meta:
        model = user_university
        fields = ["university"]
        widgets={
            "university":forms.Select(
                attrs={
                    "class":"form-control",
                    "style":"width:100%; margin-bottom:20px;",
                    "placeeholder":"University Name",
                },
            ),
        }
       