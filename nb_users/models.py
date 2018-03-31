from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

	# create a relationship (dont inherit from User!)
	user= models.OneToOneField(User, on_delete= models.CASCADE)

	# additional attributes we want
	portfolio_site= models.URLField(blank= True)
	profile_pic= models.ImageField(upload_to= 'profile_pics_folder', blank= True)

	class Meta:
		verbose_name_plural= 'User Profiles'

	def __str__(self):
		return self.user.username


class Employee(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	department= models.CharField(max_length= 100)


	def __str__(self):
		return self.user.username



