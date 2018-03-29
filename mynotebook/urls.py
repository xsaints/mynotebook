from django.conf.urls import url

from mynotebook import views

app_name= 'mynotebook'

urlpatterns= [

	url(r'^$', views.index, name= 'index'),

	# list all topics
	url(r'^topics/$', views.all_topics, name= 'all_topics'),


	# list specific topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.specific_topic, name= 'specific_topic'),


	# add a new topic
	url(r'^new_topic/$', views.new_topic, name= 'new_topic'),

	# add a new entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name= 'new_entry'),

	# edit an entry
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name= 'edit_entry'),	

]