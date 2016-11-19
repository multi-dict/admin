from django.db import models
from languages.models import Language

class Dictionary(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	languages = models.ManyToManyField(Language)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Dictionary'
		verbose_name_plural = 'Dictionaries'