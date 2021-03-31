from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Exercise, ExerciseAnswerOption


class ExerciseAnswerOptionInline(admin.StackedInline):
    model = ExerciseAnswerOption


@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    inlines = [ExerciseAnswerOptionInline]
    summernote_fields = ('description',)

    list_display = ('title', 'get_topic_title')

    def get_topic_title(self, article):
        return article.topic.title

    get_topic_title.short_description = 'тема'


