from django.contrib import admin
from .models import Dictionary
from words.models import Entity, Word
from nested_admin import NestedTabularInline, NestedModelAdmin, NestedStackedInline

class WordInline(NestedTabularInline):
    model = Word
    classes = ('grp-collapse grp-open',)
    extra = 0

class EntityInline(NestedTabularInline):
    model = Entity
    inlines = [WordInline]
    extra = 0

class DictionaryAdmin(NestedModelAdmin):
    inlines = [EntityInline]
    class Media:
        js = (
            'dictionaries/js/myscript.js',
        )

admin.site.register(Dictionary, DictionaryAdmin)

