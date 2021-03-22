from django.db import models


class ExerciseAnswerOption(models.Model):
    option = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.option)



class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    correct_option = models.ForeignKey(
        ExerciseAnswerOption,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self) -> str:
        return str(self.title)


class ExerciseReport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='reports')
    answer = models.ForeignKey(ExerciseAnswerOption, on_delete=models.CASCADE, related_name='reports')
