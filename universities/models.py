from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class University_Details(models.Model):
    university_name = models.CharField(max_length=100, null=False)
    Est_Date = models.DateField(null=False)
    University_Description = models.CharField(
        max_length=200, null=False, default="")
    Vice_Chancellor = models.CharField(max_length=40, null=False)
    Chancellor = models.CharField(max_length=40, null=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="university_detail_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="university_detail_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'University_Details'
        verbose_name_plural = 'University_Details'

    def __str__(self):
        return self.university_name


class user_university(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    university = models.ForeignKey(
        University_Details, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_university_created_by",
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_university_updated_by",
    )
    updated_dt = models.DateTimeField(auto_now=True)
