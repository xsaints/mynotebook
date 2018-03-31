from django.conf.urls import url

from nb_users import views


app_name= 'nb_users'

urlpatterns= [

	# index page for users
	url('^$', views.users, name= 'nb_users'),

	# registration
	url('^register/$', views.register, name= 'register'),

]