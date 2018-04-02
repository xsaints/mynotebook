from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
#from django.http import HttpResponse

from . import models


# Create your views here.
'''
def index(request):
	return render(request, 'myblog/home.html')


class CBView(View):
	def get(self, request):
		return HttpResponse("class based views are cool!")
'''

class IndexView(TemplateView):
	template_name= 'myblog/index.html'



class PostListView(ListView):
	context_object_name= 'posts'
	model= models.Post




class PostDetailView(DetailView):
	context_object_name= 'post'
	model= models.Post
	template_name= 'myblog/post_detail.html'
