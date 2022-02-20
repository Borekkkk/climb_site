from django.contrib import admin

from .models import Question, Choice, Voie


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class VoieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['difficulty']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Voie, VoieAdmin)