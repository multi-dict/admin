from django.contrib import admin
from .models import Words

class WordsAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Words, WordsAdmin)

