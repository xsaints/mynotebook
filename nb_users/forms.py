from django import forms
from django.contrib.auth.models import User

from nb_users.models import UserProfileInfo, Employee


class UserForm(forms.ModelForm):
	password= forms.CharField(widget= forms.PasswordInput())

	class Meta:
		model= User
		fields= ['username', 'email', 'password']


class UserProfileInfoForm(forms.ModelForm):

	class Meta:
		model= UserProfileInfo
		#exclude= ('user',)
		fields= ['portfolio_site', 'profile_pic']

class EmployeeForm(forms.ModelForm):

	class Meta:
		model= Employee
		fields= ['department']