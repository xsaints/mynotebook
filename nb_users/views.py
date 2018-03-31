from django.shortcuts import render
from django.urls import reverse

from nb_users.forms import UserForm, UserProfileInfoForm


# Create your views here.
def users(request):
	return render(request, 'nb_users/users.html')


def register(request):	
	registered= False

	user_form= UserForm()
	profile_form= UserProfileInfoForm()
	if request.method== 'POST':
		user_form= UserForm(data= request.POST)
		profile_form= UserProfileInfoForm(data= request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user= user_form.save()
			user.set_password(user.password)
			user.save()

			
			profile= profile_form.save(commit= False)
			profile.user= user

			if 'profile_pic' in request.FILES:
				profile.profile_pic= request.FILES['profile_pic']

			profile.save()
			
			registered= True

		else:	# if any error
			print('error')
			print(user_form.errors) #, profile_form.errors)

	return render(request, 'nb_users/register.html', {'registered': registered, 'user_form': user_form, 'profile_form': profile_form})	