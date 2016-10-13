from django.db import models
from languages.models import Languages

class Dictionaries(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	languages = models.ManyToManyField(Languages)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Dictionary'
		verbose_name_plural = 'Dictionaries'