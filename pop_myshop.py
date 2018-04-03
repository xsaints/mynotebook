import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xx0027_main.settings')

import django
django.setup()


import random
from myshop.models import Category, Product
from faker import Faker


fake_gen= Faker()
categories= ['Books', 'Electronics', 'Grocery', 'Industrial & Scientific', 'Music', 'Software', 'Toys & Games']


def add_category():
	c= Category.objects.get_or_create(name= random.choice(categories))[0]

	c.save()
	return c


def populate(N=5):
	for entry in range(N):
		c= add_category()

		#fake_url= fake_gen.url()
		#fake_date= fake_gen.date()
		#fake_name= fake_gen.company()
		fake_text= fake_gen.catch_phrase()
		fake_dt= fake_gen.date_time()


		product= Product.objects.get_or_create(category= c, name= fake_text)[0]

		#acc_rec= AccessRecord.objects.get_or_create(name= webpg, date= fake_date)[0]


if __name__ == '__main__':
	populate(50)