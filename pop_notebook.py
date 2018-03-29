import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xx0027_main.settings')

import django
django.setup()


import random
from mynotebook.models import Topic, Entry
from faker import Faker


fake_gen= Faker()
topics= ['Books', 'Stocks', 'Python', 'Django', 'Music', 'Goals', 'Plans']


def add_subject():
	t= Topic.objects.get_or_create(subject= random.choice(topics))[0]
	t.save()
	return t


def populate(N=5):
	for entry in range(N):
		xtopic= add_subject()

		#fake_url= fake_gen.url()
		#fake_date= fake_gen.date()
		#fake_name= fake_gen.company()
		fake_text= fake_gen.text()


		entrylog= Entry.objects.get_or_create(topic= xtopic, text= fake_text)[0]

		#acc_rec= AccessRecord.objects.get_or_create(name= webpg, date= fake_date)[0]


if __name__ == '__main__':
	populate(50)