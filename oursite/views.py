# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from chatmaster.p2p_chat import *
from customauth.models import MyUser
# Create your views here.
from django.contrib.auth.decorators import login_required
client_count=0
root=[]

def home(request):
	return render(request,'home.html')

def about_us(request):
	return render(request,'aboutus.html')

def guidelines(request):
	return render(request,'guidelinesforstudent.html')

def courses_offered(request):
	return render(request,'coursesoffered.html')

def credit_grading_system(request):
	return render(request,'creditandgrading.html')

def students_register(request):
	return render(request,'Registerstudent.html')

def student_login(request):
	return render(request,'Loginstudent.html')

def college_register(request):
	return render(request,'Registercollege.html')

def mou(request):
	return render(request,'MoU.html')

def dept_wise_collaboration(request):
	return render(request,'Deptwisecollaboration1.html')

def mciee_link(request):
	return redirect('https://www.mciieiitbhu.org/')

def mobility_info(request):
	return render(request,'MobilityInfocollege.html')

def contact_us(request):
	return render(request,'ContactUs.html')

@login_required(login_url='/site/student-login/')
def chat(request):
	global client_count
	client_count+=1
	root = tk.Tk()
	root.lift()
	root.attributes('-topmost',True)
	p2p_chat = P2pChat(master=root)
	p2p_chat.mainloop()
	return redirect('/site/contact-us')

def college(request):
	return render(request,'college.html',{'object_list':MyUser.objects.filter(is_college=True)})


