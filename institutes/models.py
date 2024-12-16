from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _
from universities.models import University_Details
# Create your models here.


class Institute_type(models.Model):
    inst_type_name = models.CharField(max_length=100, null=False)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_type_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_type_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.inst_type_name


class Institute_Details(models.Model):
    inst_name = models.CharField(max_length=100, null=False)
    inst_address = models.CharField(max_length=200, null=False, default="")
    inst_pincode = models.CharField(
        max_length=6,
        validators=[RegexValidator('^[0-9]{6}$', _('Invalid pin code'))],
    )
    uni_id = models.ForeignKey(
        University_Details, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="institute_detail_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="institute_detail_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Institute_Details'
        verbose_name_plural = 'Institute_Details'

    def __str__(self):
        return self.inst_name


class Registration_Authority(models.Model):
    ra_name = models.CharField(max_length=100, null=False)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Registration_Authority_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Registration_Authority_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ra_name


class Institute_Registration_Authority(models.Model):
    inst_id = models.ForeignKey(Institute_Details, on_delete=models.CASCADE)
    ra_id = models.ForeignKey(Registration_Authority, on_delete=models.CASCADE)
    reg_date = models.DateField()
    code = models.PositiveIntegerField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_Registration_Authority_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_Registration_Authority_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Institute_Inst_type(models.Model):
    inst_id = models.ForeignKey(Institute_Details, on_delete=models.CASCADE)
    inst_type_id = models.ForeignKey(Institute_type, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_Inst_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Institute_Inst_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #   return self.inst_type_id
