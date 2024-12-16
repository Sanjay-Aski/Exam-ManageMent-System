from django.db import models
from django.contrib.auth.models import User
from universities.models import University_Details
from institutes.models import Institute_type, Institute_Details

# Create your models here.
class Program(models.Model):
    prog_name=models.CharField(max_length=200, null=False)
    prog_duration=models.CharField(max_length=200, null=False)
    prog_desc=models.CharField(max_length=200, null=False)
    prog_university=models.ForeignKey(University_Details,on_delete=models.SET_NULL,null=True)
    prog_inst_type_id=models.ForeignKey(Institute_type,on_delete=models.SET_NULL,null=True)
    prog_inst_id=models.ForeignKey(Institute_Details,on_delete=models.SET_NULL,null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Program_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Program_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prog_name
    
    def get_university(self):
        return self.prog_university.university_name     
    

class Program_Revision(models.Model):
    prog=models.ForeignKey(Program,on_delete=models.CASCADE)
    prog_rev_start_dt=models.DateField()
    prog_rev_end_dt=models.DateField()
    prog_rev_name=models.CharField(max_length=200, null=False)
    prog_rev_desc=models.CharField(max_length=200, null=False)
    prog_rev_status=models.CharField(max_length=200, null=False)
    
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Program_Revision_created_by"
    )
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="Program_Revision_updated_by"
    )
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prog_rev_name
    
    def get_program(self):
        return self.prog.prog_name
    

    