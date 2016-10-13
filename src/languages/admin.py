from django.contrib import admin
from .models import Languages

class LanguagesAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Languages, LanguagesAdmin)

