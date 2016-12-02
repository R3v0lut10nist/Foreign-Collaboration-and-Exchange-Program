import re
from django import forms
from customauth.models import MyUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class LoginForm(forms.Form):
 
    email = forms.EmailField(widget=forms.EmailInput(attrs=dict(required=True, max_length=30)), label=_("Email-Address"))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
   
    def clean_username(self):
        try:
            user = MyUser.objects.get(email__exact=self.cleaned_data['email'])
        except MyUser.DoesNotExist:
        	self.add_error('email',_("there is no such username"))
        return self.cleaned_data
        #raise forms.ValidationError(_("The username already exists. Please try another one."))
    def clean(self):
        auth=authenticate(email=self.cleaned_data['email'],password=self.cleaned_data['password'])
        if(auth is None):
            self.add_error(None,forms.ValidationError(_('Username Or Password is Incorrect')))
        return self.cleaned_data    


class EditForm(forms.ModelForm):
	class Meta:
		model=MyUser
		fields=['first_name','last_name','address']
	def clean(self):
		return self.cleaned_data