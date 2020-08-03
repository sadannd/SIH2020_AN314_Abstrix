from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Patient_Register1,Doctor_Register1,TestChange,Patient_Treatment,Patient_Treatment_Diagnosis,Patient_Treatment_Medicines,Sih_abstrix_admin
from django.contrib.sessions.models import Session
import datetime
# Create your views here.

def index(request):
    change1 = TestChange()
    change1.name = 'ABC'
    change1.job = 'Job1'
    change1.img = 'team1.png'
   
    change2 = TestChange()
    change2.name = 'PQR'
    change2.job = 'Job2'
    change2.img = 'team2.png'

    change3 = TestChange()
    change3.name = 'XYZ'
    change3.job = 'Job3'
    change3.img = 'team3.png'

    changes = [change1,change2,change3]
    
    ##Following is used for fetching from Database 
    #changes = TestChange.objects.all()

    return render(request,'index.html',{'changes': changes})

def about(request):
    return render(request,'about.html')  

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')



def home(request):
    return render(request,'index.html') 

def login(request):
    return render(request,'login.html')   

def main(request):
    return render(request,'main.html')

def signup(request):
    return render(request,'signup.html')
    
def index_icon(request):
    return render(request,'index.html')

def register_patient(request):
    p_first_name = request.POST['first-name']
    p_last_name = request.POST['last-name']
    p_number = request.POST['contact-number']
    p_password1 = request.POST['password1']
    p_password2 = request.POST['password2']

    register_p = Patient_Register1(p_first_name=p_first_name,p_last_name=p_last_name,p_number=p_number,p_password1=p_password1,p_password2=p_password2)
    register_p.p_gender = 0
    register_p.p_email = 0
    register_p.p_height = 0
    register_p.p_img = 0
    register_p.p_weight = 0
    register_p.p_aadhar = 0
    register_p.p_address = 0
    register_p.p_age = 0
    register_p.p_city = 0
    register_p.p_state = 0
    register_p.p_postal = 0
    register_p.p_bloodgroup = 0
    register_p.save()
    
    object_patient_register = Patient_Register1.objects.get(p_number = p_number)
    context_data = {
        'p_firstname': object_patient_register.p_first_name,
        'p_lastname': object_patient_register.p_last_name,
        'p_contact': object_patient_register.p_number
    }
    
    return render(request, 'signup_info_patient.html',context_data)

    
def register_doctor(request):
    d_first_name = request.POST['first-name']
    d_last_name = request.POST['last-name']
    d_number = request.POST['contact-number']
    d_password1 = request.POST['password1']
    d_password2 = request.POST['password2']

    register_d = Doctor_Register1(d_first_name=d_first_name,d_last_name=d_last_name,d_number=d_number,d_password1=d_password1,d_password2=d_password2)
    register_d.d_license_number = 0
    register_d.d_practice = 0
    register_d.d_specialization = 0
    register_d.d_email = 0
    register_d.d_qualification = 0
    register_d.d_img = 0
    register_d.d_gender = 0
    register_d.d_state = 0
    register_d.d_age = 0
    register_d.d_address = 0
    register_d.d_city = 0
    register_d.d_postal = 0
    register_d.save()
    
    object_doctor_register = Doctor_Register1.objects.get(d_number = d_number)
    context_data = {
        'd_firstname': object_doctor_register.d_first_name,
        'd_lastname': object_doctor_register.d_last_name,
        'd_contact': object_doctor_register.d_number
    }
    print(context_data)
    return render(request, 'signup_info_doctor.html', context_data)
    
def register_info_patient(request):
    if request.method == 'POST':
        p_first_name = request.POST['p-first-name']
        p_last_name = request.POST['p-last-name']
        p_number = request.POST['p-contact']
        p_email = request.POST['p-email']
        p_aadhar = request.POST['p-aadhaar']
        p_gender = request.POST['p-gender']
        p_age = request.POST['p-age']
        p_address = request.POST['p-address']
        p_city = request.POST['p-city']
        p_state = request.POST['p-state']
        p_postal = request.POST['p-postal']
        
        p_weight = request.POST['p-weight']
        p_profile_image = request.POST['p-profile-img']
        p_country = request.POST['p-country']
        p_bloodgroup = request.POST['p-blood']
        

        if Patient_Register1.objects.filter(p_first_name= p_first_name ,p_last_name = p_last_name,p_number = p_number). count()>0:

            register_info_p = Patient_Register1.objects.get(p_number = p_number) 
            register_info_p.p_email = p_email
            register_info_p.p_aadhar = p_aadhar
            register_info_p.p_gender = p_gender
            register_info_p.p_age = p_age
            register_info_p.p_city = p_city
            register_info_p.p_state = p_state
            register_info_p.p_postal = p_postal
            register_info_p.p_img = p_profile_image
            register_info_p.p_address = p_address
            register_info_p.p_weight = p_weight
            register_info_p.p_country = p_country
            register_info_p.p_bloodgrp = p_bloodgroup
            register_info_p.save()
            print("Done")
            return redirect('login')
        else:
            print("Error")
       

def register_info_doctor(request):
    if request.method == 'POST':
        d_first_name = request.POST['d-first-name']
        d_last_name = request.POST['d-last-name']
        d_number = request.POST['d-contact-number']
        d_email = request.POST['d-email']
        
        d_gender = request.POST['d-gender']
        d_age = request.POST['d-age']
        d_regNo = request.POST['d-RegNo']
        d_qualification = request.POST['d-qualification']
        d_specialization = request.POST['d-specialization']
        d_practice = request.POST['d-practicetime']
        d_address = request.POST['d-address']
        d_city = request.POST['d-city']
        d_state = request.POST['d-state']
        d_postal = request.POST['d-postal']
        d_profile_image = request.POST['d-profile-image']
        d_country = request.POST['d-country']

        if Doctor_Register1.objects.filter(d_first_name= d_first_name ,d_last_name = d_last_name,d_number = d_number). count()>0:

            register_info_d = Doctor_Register1.objects.get(d_number = d_number) 
            register_info_d.d_email = d_email
            
            register_info_d.d_gender = d_gender
            register_info_d.d_age = d_age
            register_info_d.d_license_number = d_regNo
            register_info_d.d_qualification = d_qualification
            register_info_d.d_specialization = d_specialization
            register_info_d.d_practice = d_practice
            register_info_d.d_city = d_city
            register_info_d.d_state = d_state
            register_info_d.d_postal = d_postal
            register_info_d.d_img = d_profile_image
            register_info_d.d_address = d_address
            register_info_d.d_country = d_country
            register_info_d.save()
            print("Done")
            return redirect('login')
        else:
            print("Error")
   

def login_patient(request):

    p_uid = request.POST['p-unique-id3']
    print(p_uid)
    old_patient = Patient_Register1.objects.get(p_unique_id = p_uid)
    patient_history1 = Patient_Treatment_Diagnosis.objects.filter(p_unique_id = p_uid).only('p_caseno', 'p_symptoms','d_uid').order_by('id')
    print(patient_history1)
    p_appointment1 = []
    p_appointment2 = []
    p_appointment3 = []
    for i in patient_history1:
        p_appointment1.append(i.d_uid)
        p_appointment2.append(i.p_caseno)
        p_appointment3.append(i.p_symptoms)
            
    print(p_appointment1)    
    print(p_appointment2)
    print(p_appointment3)
    
    patient_history2 = Patient_Treatment.objects.filter(p_unique_id = p_uid, d_uid__in = p_appointment1).only('t_date').order_by('id')
    p_appointment2 = []
    for i in patient_history2:
        p_appointment2.append(i.t_date)
            
    print(p_appointment2)
    main4 = zip(patient_history1,patient_history2)
    data = {
        "p_gender":old_patient.p_gender,
        "p_age":old_patient.p_age,
        "p_bloodgrp":old_patient.p_bloodgrp,
        "p_city":old_patient.p_city,
        "p_state":old_patient.p_state,
        "p_uid":old_patient.p_unique_id,
        'main4': main4,
    
    }
    return render(request,"patient_home.html",data)

def login_doctor(request):
        d_number1 = None
        if request.method == 'POST':
            d_number1 = request.POST['contact-number']
            d_password = request.POST['password']
            print(d_number1, d_password)

            if Doctor_Register1.objects.filter(d_number = d_number1, d_password1 = d_password). count() > 0:
                request.session['doctor_num'] = d_number1
                object1 = Doctor_Register1.objects.get(d_number = d_number1)
                d_id = request.session['doctor_id'] = object1.pk
                d_name = request.session['doctor_name'] = object1.d_first_name
                
                #Gathering p_id from patient treatment table
                patient_info_id = Patient_Treatment.objects.filter(d_uid = d_id)
                p_list_id = []
                for i in patient_info_id:
                    p_list_id.append(i.p_unique_id)
                print(p_list_id)
                
                #p_name = []
                #p_diagnosis = []
                patient_info_id1 = Patient_Treatment.objects.filter(p_unique_id__in = p_list_id, d_uid = d_id).order_by('id')
                patient_info_id3 = Patient_Treatment_Diagnosis.objects.filter(p_unique_id__in = p_list_id, d_uid = d_id ).only('p_unique_id','p_infection', 'p_diagnosis').order_by('id')
                
                main2 = zip(patient_info_id1,patient_info_id3)
                print("df",patient_info_id1)
                print("df1",patient_info_id3)
                contect_data = {
                    "main2":main2,
                    "dname":d_name,
                } 
                return render(request, 'doctor_home.html',contect_data)
            else:
                print("Invalid Data")
                return redirect('login')

        else:
            return redirect('login') 

def logout1(request):

    #request.session['patient_num'] = None
    #request.session['patient_name'] = None
    #for key in request.session.keys():
     #   del request.session[key]
    return redirect('login')

def add_patient_1(request):
    d_name = request.session['doctor_name']
    context_data = {
        "dname":d_name,
    }
    return render(request, 'add_patient_1.html',context_data)

def add_patient_1_verification(request):

    if request.method == 'POST':
        p_mobile = request.POST['p-mobile']
        
        object_patient_register = Patient_Register1.objects.get(p_number = p_mobile)
        pid = object_patient_register.pk
        d_name = request.session['doctor_name']
        print(pid)
        patient_history1 = Patient_Treatment_Diagnosis.objects.filter(p_uid = pid).only('p_caseno', 'p_symptoms','d_uid').order_by('id')
        print(patient_history1)
        p_appointment1 = []
        p_appointment2 = []
        p_appointment3 = []
        
        for i in patient_history1:
            p_appointment1.append(i.d_uid)
            p_appointment2.append(i.p_caseno)
            p_appointment3.append(i.p_symptoms)
            
        print(p_appointment1)    
        print(p_appointment2)
        print(p_appointment3)

        patient_history2 = Patient_Treatment.objects.filter(p_uid = pid, d_uid__in = p_appointment1).only('t_date').order_by('id')

        p_appointment2 = []
        for i in patient_history2:
            p_appointment2.append(i.t_date)
            
        print(p_appointment2) 

        #patient_history3 = Doctor_Register1.objects.filter(id__in = p_appointment).order_by('id')

        #p_appointment3 = []
        #for i in patient_history3:
        #    p_appointment3.append(i.d_first_name)
            
       # print(p_appointment3)

        patient_medical_history = Patient_Treatment_Medicines.objects.filter(p_uid = pid)
        pcase_list = []
        pmed_list = []
        p_dur_list = []

        for i in patient_medical_history:
            pcase_list.append(i.p_caseno)
            pmed_list.append(i.p_medicine)
            p_dur_list.append(i.p_med_duration)

        print("case no",pcase_list) 
        print("med list",pmed_list)
        print("p_dur",p_dur_list)



        main3 = zip(patient_history1,patient_history2)
        context_data = {
        'p_firstname': object_patient_register.p_first_name,
        'p_lastname': object_patient_register.p_last_name,
        'p_contact': object_patient_register.p_number,
        'p_email': object_patient_register.p_email,
        'p_address': object_patient_register.p_address,
        'p_country': object_patient_register.p_country,
        'p_city': object_patient_register.p_city,
        'p_state': object_patient_register.p_state,
        'p_postal': object_patient_register.p_postal,
        'p_pic': object_patient_register.p_img,
        'p_gender': object_patient_register.p_gender,
        'p_bloodgrp': object_patient_register.p_bloodgrp,
        'p_age' : object_patient_register.p_age,
        'main3': main3,
        "dname":d_name
        
        }


    


             
        
        

    return render (request, "add_patient_2.html", context_data)

def doctor_dashboard(request):

    return render(request,"doctor_dashboard.html")

def patient_treatment(request):
    if request.method =='POST':
        x = datetime.datetime.now()
        date = x.strftime("%Y-%m-%d")
        time = x.strftime("%X")
        day = x.strftime("%A")
        d_uid = request.POST['d-uid']
        p_caseno = request.POST['p-caseno']
        p_unique_id = request.POST['p-unique-id']
        p_gender = request.POST['p-gender']
        p_age = request.POST['p-age']
        p_city = request.POST['p-city']
        p_blood = request.POST['p-bloodgrp']
        p_state = request.POST['p-state']

        print(p_unique_id)
        #object1 = Patient_Register1.objects.get(p_unique_id = p_unique_id)
        #p_id = object1.pk
        #request.session['p_id'] = p_id
        request.session['p_caseno'] = p_caseno
       
        object2 = Patient_Treatment()
        object2.t_date = date
        object2.t_day =day
        object2.t_time = time
        object2.d_uid = d_uid
        object2.p_unique_id = p_unique_id
        object2.p_caseno = p_caseno
        object2.p_bloodgrp = p_blood
        object2.p_city = p_city
        object2.p_state = p_state
        object2.p_age = p_age
        object2.p_gender = p_gender
        
        object2.save()
        context_treatment = {
          'p_unique_id' : object2.p_unique_id,
           'p_caseno': object2.p_caseno
        }
        print("Done")
        return render(request,"add_patient_2.html", context_treatment)
    else:
        print("Error")    

def patient_prescription(request):
    if request.method == 'POST':
        d_uid = request.session['doctor_id']
        p_unique_id = request.POST['p-unique-id']
        p_caseno = request.POST['p-caseno']
        p_infection = request.POST['p-infection']
       
        p_symptoms = request.POST['p-symptoms']
        p_weight = request.POST['p-weight']
        p_bp = request.POST['p-bp']
        p_diagnosis = request.POST['p-diagnosis']
        #m-med-morn = request.POST.get('m-morning',0)
        #m-med-after = request.POST.get('m-afternoon',0)
        #m-med-night = request.POST.get('m-night',0)
        


        l_data = []
        for k in request.POST.values():
             l_data.append(k)
        print(l_data)
        print(len(l_data))  
        l_data = l_data[1:]
        print(len(l_data))   

        object1 = Patient_Treatment_Diagnosis()
        object1.d_uid = d_uid
        object1.p_unique_id = p_unique_id
        object1.p_caseno = p_caseno
        object1.p_infection = p_infection
        object1.p_symptoms = p_symptoms
        object1.p_weight = p_weight
        object1.p_bp = p_bp
        object1.p_diagnosis = p_diagnosis
        object1.save()

        for i in range(7,len(l_data)-2,5):
            object2 = Patient_Treatment_Medicines()
            object2.p_unique_id = p_unique_id
            object2.p_caseno = p_caseno
            object2.p_medicine = l_data[i].strip()
            object2.p_med_duration = int(l_data[i+1].strip())
            object2.p_med_morning = int(l_data[i+2].strip())
            object2.p_med_afternoon = int(l_data[i+3].strip())
            object2.p_med_night = int(l_data[i+4].strip())
            #object2.p_med_antibiotic = int(l_data[i+5].strip())
            object2.save()



    return render(request, "add_patient_2.html")


def sih_useradmin(request):

    return render(request,"login_admin_new2.html")

def sih_admin_signup(request):
    if request.method == 'POST':
        a_first_name = request.POST['a-first-name']
        a_last_name = request.POST['a-last-name']
        a_number = request.POST['a-number']
        a_password1 = request.POST['a-password1']
        a_password2 = request.POST['a-password2']

        register_a = Sih_abstrix_admin()
        register_a.a_first_name = a_first_name
        register_a.a_last_name = a_last_name
        register_a.a_number = a_number
        register_a.a_password1 = a_password1
        register_a.a_password2 = a_password2

        register_a.save()

    return render(request,"login_admin_new2.html")

def sih_admin_login(request):

    if request.method =='POST':
        a_number = request.POST['a-number']
        a_password = request.POST['a-password']

        if Sih_abstrix_admin.objects.filter(a_number = a_number, a_password1 = a_password).count()>0:
            object1 = Sih_abstrix_admin.objects.get(a_number = a_number)
            a_name = object1.a_first_name
            request.session['admin-name'] = a_name


            return render(request,"admin_dashboard_new.html",{"aname":a_name})
        else: 
            print("Invalid Data")  
            return redirect('sih_useradmin')  

    else:
        return redirect('sih_useradmin')

def close_case(request):

    return render(request,'doctor_home.html')
        
def logout1_admin(request):
    return render (request,"login_admin_new.html")    
    
def add_patient_new(request):
    p_gender = request.POST['p-gender1']
    p_age = request.POST['p-age']
    p_bloodgrp = request.POST['p-blood']
    p_state = request.POST['p-state']
    p_city = request.POST['p-city']
    p_uid = request.POST['p-uid']

    new_patient = Patient_Register1(p_gender = p_gender, p_age = p_age, p_bloodgrp = p_bloodgrp, p_state = p_state,p_city = p_city, p_unique_id = p_uid)
    new_patient.save()
    text1 = "Patient Registered"
    data = {
        "msg" : text1,
        "p_gender":p_gender,
        "p_age":p_age,
        "p_bloodgrp":p_bloodgrp,
        "p_city":p_city,
        "p_state":p_state,
        "p_uid":p_uid
    }
    return render(request,"add_patient_2.html",data)



def add_patient_old(request):
    p_uid = request.POST['p-unique2']
    print(p_uid)
    old_patient = Patient_Register1.objects.get(p_unique_id = p_uid)
    patient_history1 = Patient_Treatment_Diagnosis.objects.filter(p_unique_id = p_uid).only('p_caseno', 'p_symptoms','d_uid').order_by('id')
    print(patient_history1)
    p_appointment1 = []
    p_appointment2 = []
    p_appointment3 = []
    for i in patient_history1:
        p_appointment1.append(i.d_uid)
        p_appointment2.append(i.p_caseno)
        p_appointment3.append(i.p_symptoms)
            
    print(p_appointment1)    
    print(p_appointment2)
    print(p_appointment3)
    
    patient_history2 = Patient_Treatment.objects.filter(p_unique_id = p_uid, d_uid__in = p_appointment1).only('t_date').order_by('id')
    p_appointment2 = []
    for i in patient_history2:
        p_appointment2.append(i.t_date)
            
    print(p_appointment2)
    main3 = zip(patient_history1,patient_history2)
    data = {
        "p_gender":old_patient.p_gender,
        "p_age":old_patient.p_age,
        "p_bloodgrp":old_patient.p_bloodgrp,
        "p_city":old_patient.p_city,
        "p_state":old_patient.p_state,
        "p_uid":old_patient.p_unique_id,
        'main3': main3,
    
    }
    return render(request,"add_patient_2.html",data)
       






    





