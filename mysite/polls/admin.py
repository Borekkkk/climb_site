from django.contrib import admin

from .models import Question, Choice, Voie, Site, Secteur


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]


class SecteurAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['site']})
    ]


class VoieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['site']}),
        (None, {'fields': ['secteur']}),
        (None, {'fields': ['difficulty']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Voie, VoieAdmin)
admin.site.register(Secteur, SecteurAdmin)
admin.site.register(Site, SiteAdmin)
