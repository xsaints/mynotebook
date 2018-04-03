from django.conf.urls import url

from myshop import views

app_name= 'myshop'  

  
urlpatterns= [

	url(r'^$', views.index, name= 'index'),

	url(r'categories/$', views.CategoryListView.as_view(), name= 'categories'),

	url(r'categories/(?P<pk>\d+)', views.CategoryProductsDetailView.as_view(), name= 'category_products'),

	url(r'categories/create/$', views.CategoryCreateView.as_view(), name= 'category_create'),

	url(r'categories/update/(?P<pk>\d+)/$', views.CategoryUpdateView.as_view(), name= 'category_update'),	


]    
