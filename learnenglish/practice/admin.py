from django.contrib import admin

from .models import Exercise, ExerciseAnswerOption


class ExerciseAnswerOptionInline(admin.StackedInline):
    model = ExerciseAnswerOption


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [ExerciseAnswerOptionInline]
