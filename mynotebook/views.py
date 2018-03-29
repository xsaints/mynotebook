from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse


from mynotebook.models import Topic, Entry
from mynotebook.forms import TopicForm, EntryForm



# Create your views here.
def index(request):
	return render(request, 'mynotebook/index.html')


def all_topics(request):
	topics= Topic.objects.all()
	return render(request, 'mynotebook/all_topics.html', {'topics': topics})	


def specific_topic(request, topic_id):
	topic= Topic.objects.get(id= topic_id)
	entries= topic.entry_set.all()
	return render(request, 'mynotebook/specific_topic.html', {'topic': topic, 'entries': entries})	


def new_topic(request):
	form= TopicForm()

	if request.method == 'POST':
		form= TopicForm(request.POST)
		if form.is_valid():
			#print(request.POST['subject'])
			#print("hello world!")
			form.save()
			return HttpResponseRedirect(reverse('ns_notebook:all_topics'))

	return render(request, 'mynotebook/new_topic.html', {'form': form})