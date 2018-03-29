from django.db import models

# Create your models here.

class Topic(models.Model):
	subject= models.CharField(max_length= 100, unique= True)
	date_added= models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.subject


class Entry(models.Model):
	topic= models.ForeignKey(Topic, on_delete= models.CASCADE)		
	text= models.TextField()
	entry_date= models.DateTimeField(auto_now_add= True)
	#last_update= models.DateField(auto_now= True)

	class Meta:
		verbose_name_plural= 'entries'
		
	def __str__(self):
		return self.text[:50] + '...'