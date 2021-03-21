from django.db import models


class ExerciseAnswerOption(models.Model):
    option = models.CharField(max_length=200)


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4096)
    correct_option = models.ForeignKey(
        ExerciseAnswerOption,
        on_delete=models.CASCADE,
    )


class ExerciseReport(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    answer = models.ForeignKey(ExerciseAnswerOption, on_delete=models.CASCADE)
