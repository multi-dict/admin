from django.db import models


class Language(models.Model):
	name = models.CharField(max_length=255, blank=False, null=False)
	ISO_2 = models.CharField(max_length=2, blank=False, null=False, unique=True)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'