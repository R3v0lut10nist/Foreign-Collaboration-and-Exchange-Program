import re
from django import forms
from customauth.models import MyUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
#CustomUser=django.contrib.auth.get_user_model()
# class RegistrationForm(forms.ModelForm):
 
#     #username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
#     email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
#     class Meta:
#         model=MyUser
#         fields=['date_of_birth']
#     def clean_username(self):
#         try:
#             user = MyUser.objects.get(username__exact=self.cleaned_data['username'])
#         except MyUser.DoesNotExist:
#             return self.cleaned_data['username']
#         raise forms.ValidationError(_("The username already exists. Please try another one."))
 
#     def clean(self):
#         #raise forms.ValidationError(_("The two password fields did not match."))
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError(_("The two password fields did not match."))
# #         return self.cleaned_data

class USERCreationForm(UserCreationForm):
    def __init__(self,*args,**kargs):
        super(USERCreationForm,self).__init__(*args,**kargs)
    class Meta:
        model=MyUser
        fields=['first_name','last_name','mobilenumber','email','address','nationality','subject','programme']
class USERUserChangeForm(UserChangeForm):
    def __init__(self,*args,**kargs):
        super(USERUserCreationForm,self).__init__(*args,**kargs)
    class Meta:
        model=MyUser
        fields=['first_name','last_name','mobilenumber','email','address','nationality','subject','programme']

class college_register(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)),label=_("College Name"))
    address=forms.CharField(widget=forms.Textarea(attrs=dict(required=True)),label=_('Address'))
    contact=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=10)),label=_('Contact No.'))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    def clean(self):
        #raise forms.ValidationError(_("The two password fields did not match."))
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

        if 'contact' in self.cleaned_data :
            if self.cleaned_data['contact'].is_digit():
                if 1000000000<self.cleaned_data['contact']<9999999999 :
                    pass
                else:
                    raise forms.ValidationError(_("Wrong contact no."))
            else :
                raise forms.ValidationError(_('Wrong contact no.'))