from django.contrib import admin
from .models import TestChange,Patient_Register1,Doctor_Register1,Med_tab1,Patient_Treatment,Patient_Treatment_Diagnosis,Patient_Treatment_Medicines
# Register your models here.

admin.site.register(TestChange)
admin.site.register(Patient_Register1)
admin.site.register(Doctor_Register1)
admin.site.register(Med_tab1)
admin.site.register(Patient_Treatment)
admin.site.register(Patient_Treatment_Diagnosis)
admin.site.register(Patient_Treatment_Medicines)
