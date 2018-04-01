from django.conf.urls import url

from nb_users import views


app_name= 'nb_users'

urlpatterns= [

	# index page for users
	url('^$', views.users, name= 'nb_users'),

	# registration
	url('^register/$', views.register, name= 'register'),

	
	# login
	url('^login/$', views.user_login, name= 'user_login'),
	#url('^login/$', views.user_login, {'template_name': 'nb_users/login.html'}, name= 'user_login'),	


	# login
	url('^logout/$', views.user_logout, name= 'user_logout'),

]