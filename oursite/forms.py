from django import forms
from customauth.models import MyUser
from django.utils.translation import ugettext_lazy as _

class FilterForm(forms.Form):
	subject=forms.CharField(widget=forms.TextInput(attrs=dict(required=False,max_length=20)), label=_("SUBJECT :"))
	first_name=forms.CharField(widget=forms.TextInput(attrs=dict(required=False,max_length=20)),label=_("NAME:"))