from django import forms

from mynotebook.models import Topic, Entry


class TopicForm(forms.ModelForm):
	class Meta:
		model= Topic
		fields= ['subject']
		label= {'subject': '',}


class EntryForm(forms.ModelForm):
	class Meta:
		model= Entry
		#exclude= ['entry_date',]
		fields= ['text',]
		labels= {'text': ''}
		widgets= {'text': forms.Textarea(attrs={'cols':80})}