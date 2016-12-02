from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from login.forms import *
from django import forms
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import *
from django.contrib.auth import authenticate, login, logout
from register.forms import *
from customauth.models import MyUser
from .models import *
@csrf_protect
def login_user(request):
    logout(request)
    email = password = ''
    form=None
    if (request.method=='POST'):
    	form=LoginForm(request.POST)
    	if(form.is_valid):
        	email = request.POST['email']
        	password = request.POST['password']

       		user = authenticate(email=email, password=password)
       		if (user is not None):

          	    if user.is_active:
          	    	login(request, user)
          	    	return HttpResponseRedirect('/site/student/profile')
    else:
    	form=LoginForm()
    return render(request,'Loginstudent.html', {'form':form})
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/site/student-login')
@login_required(login_url='login/')
def home(request):
  return render(request,'home.html',{'u':request.user , 'list':MyUser.objects.all(),})
@login_required(login_url='login/')
def edit(request):
  #u=UserProfile.objects.get(user=User.objects.get(username=request.user))
  user=MyUser.objects.get(email=request.user)
  # u=UserProfile.objects.get(user=user)
  form=EditForm(instance=user)
  if(request.method=='POST'):
    form=EditForm(request.POST,instance=user)
    if(form.is_valid):
      form.save()
    return HttpResponseRedirect('/site/student/profile')
  else:
    pass
  return render(request,'edit.html',{'form':form})