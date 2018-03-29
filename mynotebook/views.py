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
	entries= topic.entry_set.order_by('-last_update')
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


def new_entry(request, topic_id):

	topic= Topic.objects.get(id= topic_id)

	form= EntryForm()
	if request.method == 'POST':
		form= EntryForm(data= request.POST)
		if form.is_valid():
			#print(request.POST['subject'])
			#print("hello world!")
			new_entry= form.save(commit= False)	
			new_entry.topic= topic
			new_entry.save()

			return HttpResponseRedirect(reverse('ns_notebook:specific_topic', args= [topic.id]))

	return render(request, 'mynotebook/new_entry.html', {'form': form, 'topic': topic})



def edit_entry(request, entry_id):
	entry= Entry.objects.get(id= entry_id)

	#topic_id= entry.topic.id
	#topic= Topic.objects.get(id= topic_id)
	topic= entry.topic

	if request.method != 'POST':
		form= EntryForm(instance= entry)
	else:
		form= EntryForm(instance= entry, data= request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('ns_notebook:specific_topic', args= [topic.id]))

	return render(request, 'mynotebook/edit_entry.html', {'form': form, 'entry': entry, 'topic': topic})	