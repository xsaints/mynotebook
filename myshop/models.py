from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):
  name= models.CharField(max_length= 200, db_index= True, unique= True)
  #slug= models.SlugField(max_length= 200, db_index= True, unique= True)
  
  
  class Meta:
    ordering= ('name',)
    verbose_name= 'category'
    verbose_name_plural= 'categories'
    
    
  def __str__(self):
    return self.name


  def get_absolute_url(self):
    return reverse('myshop:category_products', kwargs= {'pk':self.pk })
    

class Product(models.Model):
  category= models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'products')
  
  name= models.CharField(max_length= 200, db_index= True)
  #slug= models.SlugField(max_length= 200, db_index= True)
  image= models.ImageField(upload_to= 'products/%Y/%m/%d', blank= True)
  
  class Meta:
    ordering= ('name',)
    #index_together= (('id', 'slug'),)
    
  def __str__(self):
    return self.name
