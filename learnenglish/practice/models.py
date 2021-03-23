from django.db import models

from theory.models import Topic


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    correct_option = models.ForeignKey(
        'ExerciseAnswerOption',
        on_delete=models.CASCADE,
        related_name='correct_exercises'
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topics')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self) -> str:
        return str(self.title)


class ExerciseAnswerOption(models.Model):
    option = models.CharField(max_length=200)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ на задание'
        verbose_name_plural = 'Ответы на задание'

    def __str__(self) -> str:
        return str(self.option)


class ExerciseReport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='reports')
    answer = models.ForeignKey(ExerciseAnswerOption, on_delete=models.CASCADE, related_name='reports')
