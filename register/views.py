from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from register.forms import *
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.template import RequestContext,Template,Context
from django.contrib.auth.forms import AuthenticationForm
#from login.models import UserProfile
 
raw_template='''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang='en'>
<head>
	<title>REGISTER YOURSELF</title>
</head>
<body>
	<form action="." method='POST'>{% csrf_token %}
		<table>
			{{form.as_table}}
		</table>
		<input type="submit" name="Register">
</form>
</body>
</html>'''

def register_student(request):
	form=None
	if(request.method == 'POST'):
		form=USERCreationForm(request.POST)
		if(form.is_valid()):
			# user=MyUser.objects.create_user(
			# 	#username=form.cleaned_data['username'],
			# 	password=form.cleaned_data['password1'],
			# 	email=form.cleaned_data['email'],
			# 	date_of_birth=form.cleaned_data.get(date_of_birth)
			# 	)
			student=MyUser.objects.create_user(email=form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],address=form.cleaned_data['address'],mobilenumber=form.cleaned_data['mobilenumber'],password=form.cleaned_data['password1'],is_college=False,nationality=form.cleaned_data['nationality'],subject=form.cleaned_data['subject'],programme=form.cleaned_data['programme'])
			student.save()
			return redirect('/register/success')
	else:
		form=USERCreationForm()
		t=Template(raw_template)
		c=Context({'form':form})
	return render(request,'Registerstudent.html',{'form':form})
	
def register_college(request):
	form=None
	if(request.method == 'POST'):
		form=college_register(request.POST)
		if(form.is_valid()):
			# user=MyUser.objects.create_user(
			# 	#username=form.cleaned_data['username'],
			# 	password=form.cleaned_data['password1'],
			# 	email=form.cleaned_data['email'],
			# 	date_of_birth=form.cleaned_data.get(date_of_birth)
			# 	)
			college=MyUser.objects.create_user(email=form.cleaned_data['email'],first_name=form.cleaned_data['name'],last_name="",address=form.cleaned_data['address'],mobilenumber=form.cleaned_data['contact'],password=form.cleaned_data['password1'],is_college=True,nationality='',subject='',programme='')
			college.save()
			return redirect('/register/success')
	else:
		form=college_register()
		t=Template(raw_template)
		c=Context({'form':form})
	return render(request,'Registerstudent.html',{'form':form})

def register_success(request):
    return render(request,
    'success.html',
    )