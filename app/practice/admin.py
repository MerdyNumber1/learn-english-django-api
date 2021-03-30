from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Exercise, ExerciseAnswerOption


class ExerciseAnswerOptionInline(admin.StackedInline):
    model = ExerciseAnswerOption


@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    inlines = [ExerciseAnswerOptionInline]
    summernote_fields = ('description',)

