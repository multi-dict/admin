from django.db import models
from dictionaries.models import Dictionaries
from languages.models import Languages


class Temp(models.Model):
	dictionary = models.ForeignKey(Dictionaries)
	
	class Meta:
		verbose_name = 'Translation'
		verbose_name_plural = 'Translations'

class Words(models.Model):
	language = models.ForeignKey(Languages)
	temp = models.ForeignKey(Temp)
	word = models.CharField(max_length=255)
	sex = models.CharField(choices=(('male', 'Male'), ('female', 'Female')), max_length=10, blank=True)
	description = models.CharField(max_length=255, blank=True)
	source = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.word

	class Meta:
		verbose_name = 'Word'
		verbose_name_plural = 'Words'