from django.db import models

from django.contrib.auth.models import User
#from nb_users.models import 


# Create your models here.

class Topic(models.Model):
	subject= models.CharField(max_length= 100, unique= True)
	date_added= models.DateTimeField(auto_now_add= True)
	owner= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.subject


class Entry(models.Model):
	topic= models.ForeignKey(Topic, on_delete= models.CASCADE)		
	text= models.TextField()
	entry_date= models.DateTimeField(auto_now_add= True)
	last_update= models.DateTimeField(auto_now= True)

	class Meta:
		verbose_name_plural= 'entries'
		
	def __str__(self):
		return self.text[:50] + '...'


class UsersN(models.Model):
	first_name = models.CharField(max_length=50)		
	last_name= models.CharField(max_length= 50)
	user_email= models.EmailField(unique= True)


	def __str__(self):
		return self.first_name + ' '+ self.last_name