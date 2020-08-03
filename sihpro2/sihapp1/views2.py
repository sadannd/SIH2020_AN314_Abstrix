from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Patient_Register1,Doctor_Register1,TestChange,Patient_Treatment,Patient_Treatment_Diagnosis,Patient_Treatment_Medicines,sih2020data
from django.contrib.sessions.models import Session
import datetime
from django.http import JsonResponse
from sklearn import linear_model
import pandas as pd
import pickle

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

def dash2(request):
    return render(request,"dash_get2.html")

def fun1(request, *args, **kwargs):
    #reg5=linear_model.LinearRegression()
    #dataset = pd.read_csv(r'C:\Users\khede\OneDrive\Desktop\sih2020data')
    ##reg5.fit([[dataset.a_Bacteria,dataset.a_Level,dataset.a_Year]],dataset.c_Cases)
    #print(reg5.predict([(1,3,2020)]))
    state = request.GET.get('state')
    state_age = request.GET.get('state_age')
    state_gender = request.GET.get('state_gender')
    print(state)
    #reg2 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\reg1.sav', 'rb'))
    #print(reg2.predict([(0,25,4,28,1,0,3,3)]))
    x=[]
    x1=[]
    x2=[]
    x3=[]
    if state == "values1":
        reg4 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\General1.sav', 'rb'))
        for level in range (1,5):       
            x1.append(reg4.predict([(1,level,2050)])[0])

        print(x1)
    elif state =="values2":
        reg5 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\Location2.sav', 'rb'))
        for level in range (1,5):       
            x1.append(reg5.predict([(1,level,2050)])[0])

        print(x1)
    elif state == "values3":
        reg6 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\Location3.sav', 'rb'))
        for level in range (1,5):       
            x1.append(reg6.predict([(1,level,2050)])[0])

        print("This is x1",x1)


    reg3 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\General1.sav', 'rb'))
    #reg4 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\Location1.sav', 'rb'))
    #reg5 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\Location2.sav', 'rb'))
    #reg6 = pickle.load(open(r'C:\Users\khede\OneDrive\Documents\GitHub\LocalRepoAbstrix\sihpro2\sihapp1\Location3.sav', 'rb'))
    

    labelsx = ["Level1", "Level2", "Level3", "Level4"]
    for level in range (1,5):       
        x.append(reg3.predict([(1,level,2030)])[0])
    
    print("This is x",x)

    ##for level in range (1,5):       
    ##    x1.append(reg4.predict([(1,level,2030)])[0])
    
    ##print(x1)
    #for level in range (1,5):       
    #    x2.append(reg5.predict([(1,level,2030)])[0])
    
    #print(x2)
    #for level in range (1,5):       
    #    x3.append(reg6.predict([(1,level,2030)])[0])
    
    #print(x3)
    


    data1 = {
        "labelsx":labelsx,
        "values1":x,
        "values22":x1,
        

    }
    return JsonResponse(data1)
    


def show_analysis(request, *args , **kwargs):
    bacteria_name = request.POST['bacteria-select']
    b_year = request.POST['b-year']
    print(bacteria_name)
    print(b_year)
    data_b = {
        'bname':bacteria_name,
        'byear':b_year,
    }
    return render(request,"dash_get2.html",data_b)


def dash2_data1(request, *args, **kwargs):
    return JsonResponse()

def dash2_data2(request, *args, **kwargs):
    return JsonResponse()

def dash2_data3(request, *args, **kwargs):
    return JsonResponse()    

def dash2_data4(request, *args, **kwargs):
    return JsonResponse()