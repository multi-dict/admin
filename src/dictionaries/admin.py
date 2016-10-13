from django.contrib import admin
from .models import Dictionaries
from words.models import Temp, Words
from nested_admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline

class WordsInline(NestedTabularInline):
	model = Words
	classes = ('grp-collapse grp-open',)
	extra = 0

class TempInline(NestedTabularInline):
	model = Temp
	inlines = [WordsInline]
	extra = 0

class DictionariesAdmin(NestedModelAdmin):
	inlines = [TempInline]

admin.site.register(Dictionaries, DictionariesAdmin)

