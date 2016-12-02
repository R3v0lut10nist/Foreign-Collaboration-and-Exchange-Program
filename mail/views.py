# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import smtplib

from django.shortcuts import render
from django.shortcuts import redirect
from mail.form import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from email.mime.text import MIMEText
# Create your views here.
from django.contrib.auth.decorators import login_required

def mail(request):
	form =None
	if (request.method=='POST'):
		form=MailForm(request.POST)
		if(form.is_valid()):
			fromemail=form.cleaned_data['from_email']
			password=form.cleaned_data['password1']
			toemail=form.cleaned_data['to_email']
			subject=form.cleaned_data['subject']
			#file=request.FILES['file']
			msg=form.cleaned_data['message']
			#message=handleemail(msg,subject)
			ser=smtplib.SMTP('smtp.gmail.com',587)
			ser.ehlo()
			ser.starttls()
			ser.login(str(fromemail),str(password))
			ser.sendmail(str(fromemail),[str(fromemail),str(toemail)],str(msg))
			ser.close()
			return redirect('/register/success')
	else:
		form=MailForm()
	return render(request,'ContactUs.html',{'form':form})


def handleemail(msg,subject):
	message=MIMEMultipart()
	message['Subject']=subject
	part1=MIMEText(str(msg),'plain')
	message.attach(part1)
	part2= MIMEBase('application',"octet-stream")
	part2.set_payload(file.read())
	Encoders.encode_base64(part2)
	part2.add_header('Content-Disposition', 'attachment; filename="text.txt"')
	message.attach(part2)
	return message    


