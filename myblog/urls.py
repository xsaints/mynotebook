from django.conf.urls import url

from myblog import views

app_name= 'myblog'


urlpatterns= [

	
	#url(r'^$', views.index, name= 'index'),

	#url(r'^$', views.CBView.as_view()),

	url(r'^$', views.IndexView.as_view(), name= 'index'),

	url(r'^list$', views.PostListView.as_view(), name= 'topics_list'),	


]