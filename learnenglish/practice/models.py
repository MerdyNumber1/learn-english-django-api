from django.db import models

from theory.models import Topic


class Exercise(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.CharField(max_length=4000, verbose_name='описание')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='exercises', verbose_name='Тема')

    class Meta:
        verbose_name = 'задание'
        verbose_name_plural = 'задания'

    def __str__(self) -> str:
        return str(self.title)


class ExerciseAnswerOption(models.Model):
    option = models.CharField(max_length=200, verbose_name='ответ')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='задание')
    is_correct = models.BooleanField(default=False, verbose_name='правильный ответ')

    class Meta:
        verbose_name = 'ответ на задание'
        verbose_name_plural = 'ответы на задание'

    def __str__(self) -> str:
        return str(self.option)


class ExerciseReport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='reports', verbose_name='задание')
    answer = models.ForeignKey(
        ExerciseAnswerOption,
        on_delete=models.CASCADE,
        related_name='reports',
        verbose_name='ответ'
    )
