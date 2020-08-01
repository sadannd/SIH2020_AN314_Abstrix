from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Patient_Register1,Doctor_Register1,TestChange,Patient_Treatment,Patient_Treatment_Diagnosis,Patient_Treatment_Medicines
from django.contrib.sessions.models import Session
import datetime
from django.http import JsonResponse




def dash1(request):
    return render(request,"dash_get1.html")

def get_data_test1(request, *args, **kwargs):
    patient_male = Patient_Treatment.objects.filter(p_gender = 'Male').count()
    patient_female = Patient_Treatment.objects.filter(p_gender = 'Female').count()
    infection_1 = Patient_Treatment_Diagnosis.objects.filter(p_infection = 'Viral').count()
    infection_2 = Patient_Treatment_Diagnosis.objects.filter(p_infection = 'Bacterial').count()
    infection_3 = Patient_Treatment_Diagnosis.objects.filter(p_infection = 'Fungal').count()
    infection_4 = Patient_Treatment_Diagnosis.objects.filter(p_infection = 'Parasite').count()
    print(patient_male)
    print(patient_female)
    print(infection_1)
    print(infection_2)
    print(infection_3)
    print(infection_4)
    labels= ['Male', 'Female']
    labels2 = ['Viral','Bacterial','Fungal','Parasite']
    count1 = [patient_male,patient_female]
    count2 = [infection_1,infection_2,infection_3,infection_4]
    data = {
        "Gender" : labels,
        "count1": count1,
        "Infection": labels2,
        "count2" : count2
        
    }
    return JsonResponse(data)

def get_medicine(request, *args, **kwargs):
    pcaseno = request.GET.get('pcaseno')
    p_medicine = []
    p_duration = []
    medicine1 = Patient_Treatment_Medicines.objects.filter(p_caseno=pcaseno)
    for i in medicine1:
         p_medicine.append(i.p_medicine)
         p_duration.append(i.p_med_duration)
   
    
    print(pcaseno)
    print(medicine1)
    print(p_medicine)
    print(p_duration)
    #main5 = zip(p_medicine,p_duration)
    data2 = {
        "medicines":p_medicine,
        "duration":p_duration
        

    } 
    return JsonResponse(data2)
