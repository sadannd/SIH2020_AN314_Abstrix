from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class TestChange(models.Model):
    
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

class Patient_Register1(models.Model):
    
    p_unique_id = models.CharField(max_length=100)
    p_gender = models.CharField(max_length=10)
    p_age = models.IntegerField()
    p_bloodgrp = models.CharField(max_length=100)
    p_city = models.CharField(max_length=100)
    p_state = models.CharField(max_length=100)

class Doctor_Register1(models.Model):

    d_first_name = models.CharField(max_length=100)
    d_last_name = models.CharField(max_length=100)
    d_number = models.BigIntegerField()
    d_password1 = models.CharField(max_length=100)
    d_password2 = models.CharField(max_length=100)  
    d_email = models.EmailField(max_length=254)
    d_license_number = models.BigIntegerField()
    d_gender = models.CharField(max_length=200)
    d_qualification = models.CharField(max_length=100)
    d_specialization = models.CharField(max_length=100)
    d_img = models.ImageField(upload_to='pics')
    d_age = models.IntegerField()
    d_address = models.CharField(max_length=500)
    d_city = models.CharField(max_length=100)
    d_state = models.CharField(max_length=100)
    d_postal = models.IntegerField()
    d_country = models.CharField(max_length=100)

class Med_tab1(models.Model):
    m_level1 = models.CharField(max_length=10)
    m_name1 = models.CharField(max_length=100)
    m_is_antibiotic1 = models.CharField(max_length=100)
    m_for_infection1= models.CharField(max_length=100)
    m_dose1 = models.CharField(max_length=10)
    
class Patient_Treatment(models.Model):
    t_day = models.CharField(max_length=100)
    t_date = models.DateField()
    t_time = models.TimeField()
    d_uid = models.IntegerField()
    p_unique_id = models.CharField(max_length=100)
    p_caseno = models.IntegerField()
    p_age = models.IntegerField()
    p_gender = models.CharField(max_length=100)
    p_bloodgrp = models.CharField(max_length=100)
    p_city = models.CharField(max_length=100)
    p_state = models.CharField(max_length=100)

class Patient_Treatment_Diagnosis(models.Model):
    d_uid = models.IntegerField()
    p_unique_id = models.CharField(max_length=100)
    p_caseno = models.IntegerField()
    p_infection = models.CharField(max_length=100)
    p_symptoms = models.CharField(max_length=100)
    p_weight = models.IntegerField()
    p_bp = models.CharField(max_length=100)
    p_diagnosis = models.CharField(max_length=500)
    
class Patient_Treatment_Medicines(models.Model):
    p_unique_id = models.CharField(max_length=100)
    p_caseno = models.IntegerField()
    p_medicine = models.CharField(max_length=100)
    p_med_duration = models.IntegerField()
    p_med_morning = models.CharField(max_length=10)
    p_med_afternoon = models.CharField(max_length=10)
    p_med_night = models.CharField(max_length=10)

class Sih_abstrix_admin(models.Model):
    a_first_name = models.CharField(max_length=100)
    a_last_name = models.CharField(max_length=100)
    a_number = PhoneNumberField()
    a_password1 = models.CharField(max_length=100)
    a_password2 = models.CharField(max_length=100)    
    
class sih2020data(models.Model):
    a_Location = models.CharField(max_length=100)
    a_Age = models.IntegerField()
    a_Gender = models.CharField(max_length=100)
    a_Bacteria = models.IntegerField()
    a_Level = models.IntegerField()
    a_Year = models.IntegerField()
    c_Cases = models.BigIntegerField()

