from django.shortcuts import render
from django.urls import reverse


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from nb_users.forms import UserForm, UserProfileInfoForm
from nb_users.models import UserProfileInfo



# Create your views here.
def users(request):

	return render(request, 'nb_users/users.html')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('mynotebook:index'))


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


def user_login(request):

	if request.method== 'POST':

		username= request.POST.get('username')
		password= request.POST.get('password')

		user= authenticate(username= username, password= password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('mynotebook:index'))

			else:
				return HttpResponse('Account not active')
		else:
			print("Someone tried to login and failed!")
			print('{} {}'.format(username, password))
			return HttpResponse('Invalid login details supplied!')

	else:
		return render(request, 'nb_users/login.html', {})