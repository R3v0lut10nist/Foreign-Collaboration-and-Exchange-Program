from django.conf.urls import url
from . import views
from register import views as reg_views
from mail import views as mail_views
from login import views as login_views
from django.views.generic import ListView
from customauth.models import MyUser
from customauth.views import *
app_name='login'
urlpatterns = [
		url(r'^$',views.home,name='home'),
		url(r'^about-us/$',views.about_us,name='aboutus'),
		url(r'^guidelines-courses/$',views.guidelines,name='guidelines'),
		url(r'^courses-offered/$',views.courses_offered,name='coursesoffered'),
		url(r'^credit-grading-system/$',views.credit_grading_system,name='creditgradingsystem'),
		url(r'^students/$',reg_views.register_student,name='student_register'),
		url(r'^student-login/$',login_views.login_user,name='student_login'),
		url(r'^logout/$',login_views.logout_page,name="logout"),
		url(r'^edit/$', login_views.edit, name = "edit"),
		url(r'^cregister/$',reg_views.register_college,name='college_register'),
		url(r'^mou/$',views.mou,name='mou'),
		url(r'^dept-wise-collboration/$',views.dept_wise_collaboration,name='dept_wise_collaboration'),
		url(r'^mciee-link/$',views.mciee_link,name='mciee_link'),
		url(r'^mobility-info/$',views.mobility_info,name='mobility_info'),
		url(r'^contact-us/$',mail_views.mail,name='contact_us'),
		url(r'^student/$',index,name="index"),
		url(r'^student/profile/$',profile_display,name="student_profile"),
		url(r'^chat/$',views.chat,name='chat'),
		url(r'^college__trashed/$',views.college,name='college')
	
]
