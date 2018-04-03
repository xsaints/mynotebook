from django.shortcuts import render

# Create your views here.
from django.views.generic import (View, TemplateView, ListView, DetailView,
	CreateView, UpdateView, DeleteView)

from . import models



def index(request):
	return render(request, 'myshop/index.html')

class CategoryListView(ListView):
	model= models.Category
	context_object_name= 'categories'



class CategoryProductsDetailView(DetailView):
	model= models.Category
	context_object_name= 'category'
	template_name= 'myshop/category_products.html'


class CategoryCreateView(CreateView):
	model= models.Category
	fields= ('name',)


class CategoryUpdateView(UpdateView):
	model= models.Category
	fields= ('name',)	

	