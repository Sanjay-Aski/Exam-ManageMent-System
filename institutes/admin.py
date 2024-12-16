# admin.py
from django.contrib import admin
from .models import Institute_Inst_type, Institute_type, Registration_Authority  # Import your model

admin.site.register(Institute_type)  # Register your model
admin.site.register(Institute_Inst_type)  # Register your model
admin.site.register(Registration_Authority)  # Register your model