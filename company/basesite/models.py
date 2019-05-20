from django.db import models
from django.shortcuts import reverse


class Vacancy(models.Model):
	title = models.CharField('Заголовок', max_length=150, db_index=True)
	price = models.DecimalField('З/П', max_digits=8, decimal_places=2)
	body = models.TextField(blank=True, db_index=True)


	def __str__(self):
		return '{}'.format(self.title)

class Services(models.Model):
	title = models.CharField('Заголовок', max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, unique=True)
	body = models.TextField(blank=True, db_index=True)

	def get_absolute_url(self):
		return reverse('services_detail_url', kwargs={'slug': self.slug})

	def __str__(self):
		return '{}'.format(self.title)