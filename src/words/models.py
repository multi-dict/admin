from django.db import models
from dictionaries.models import Dictionary
from languages.models import Language


class Entity(models.Model):
	dictionary = models.ForeignKey(Dictionary)
	
	class Meta:
		verbose_name = 'Entity'
		verbose_name_plural = 'Entities'

class Word(models.Model):
	language = models.ForeignKey(Language)
	entity = models.ForeignKey(Entity)
	word = models.CharField(max_length=255)
	gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female'), ('genderless', 'Genderless')), max_length=10, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	source = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.word

	class Meta:
		verbose_name = 'Word'
		verbose_name_plural = 'Words'