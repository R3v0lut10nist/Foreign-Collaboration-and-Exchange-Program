from customauth.models import MyUser
from django.views.generic import ListView
from oursite.forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    form=FilterForm()
    if(request.method=="POST"):
        form=FilterForm(request.POST)
        return redirect('/site/subject=%s&first_name=%s'.format(form.cleaned_data['subject'],form.cleaned_data['first_name']))
    form=FilterForm()
    subject = request.GET.get('subject','')
    first_name=request.GET.get('first_name','')
    programme=request.GET.get('programme','')
    if subject == "" and first_name == "" and programme=='':
        userlist = MyUser.objects.filter(is_college=False,is_admin=False).order_by("first_name")
    elif first_name == "" and programme== "":
        userlist = MyUser.objects.filter(subject=subject,is_college=False,is_admin=False).order_by("first_name")
    elif subject == "" and programme == "":
        userlist = MyUser.objects.filter(first_name=first_name,is_college=False,is_admin=False).order_by("first_name")
    elif subject == "" and first_name == "":
        userlist = MyUser.objects.filter(programme=programme,is_college=False,is_admin=False).order_by("first_name")
    elif first_name == "":
        userlist = MyUser.objects.filter(subject=subject, programme=programme,is_college=False,is_admin=False).order_by("first_name")
    elif programme == "":
        userlist = MyUser.objects.filter(subject=subject, first_name=first_name,is_college=False,is_admin=False).order_by("first_name")
    elif subject == "":
        userlist = MyUser.objects.filter(programme=programme, first_name=first_name,is_college=False,is_admin=False).order_by("first_name")
    else:
        userlist = MyUser.objects.filter(subject=subject, first_name=first_name,programme=programme,is_college=False,is_admin=False).order_by("first_name")
    return render(request, 'Deptwisecollaboration.html',{'form':form, 'object_list':userlist})

@login_required(login_url='/site/student-login/')
def profile_display(request):
	return render(request,'Profile.html',{'user':request.user})