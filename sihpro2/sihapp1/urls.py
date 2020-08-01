
from django.urls import path
from . import views,views2
#from .views2 import ChartData

urlpatterns = [
  path('',views.index, name ='index'),
  path('about', views.about, name = 'about'),
  path('blog', views.blog, name = 'blog'),
 
  path('contact', views.contact, name = 'contact'),
  
  path('home', views.home, name = 'home'),
  path('login', views.login, name = 'login'),
  path('signup', views.signup, name = 'signup'),
  path('index_icon', views.index_icon, name = 'index_icon'),
  path("register_patient", views.register_patient, name="register_patient"),
  path("register_doctor", views.register_doctor, name="register_doctor"),
  path("register_info_patient", views.register_info_patient, name="register_info_patient"),
  path("register_info_doctor", views.register_info_doctor, name="register_info_doctor"),
  path("login_doctor", views.login_doctor, name="login_doctor"),
  path("login_patient", views.login_patient, name="login_patient"),
  path("add_patient_1", views.add_patient_1, name = "add_patient_1"),
  path("add_patient_1_verification",views.add_patient_1_verification, name = "add_patient_1_verification"),
  path("doctor_dashboard",views.doctor_dashboard, name = "doctor_dashboard"),
  path("patient_treatment", views.patient_treatment, name = "patient_treatment"),
  path("patient_prescription", views.patient_prescription, name ="patient_prescription"),
  path("get_medicine", views2.get_medicine, name ="get_medicine"),

  path("dash1",views2.dash1, name = "dash1"),
  path("get_data_test1", views2.get_data_test1, name = "get_data_test1"),

  path("sih_useradmin",views.sih_useradmin, name ="sih_useradmin"),
  path("sih_admin_login",views.sih_admin_login, name ="sih_admin_login"),
  path("sih_admin_signup",views.sih_admin_signup, name ="sih_admin_signup"),
  path("close_case",views.close_case, name ="close_case"),
  

  path("logout1",views.logout1, name="logout1"),

]

