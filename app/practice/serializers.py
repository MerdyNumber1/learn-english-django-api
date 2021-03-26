from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Exercise, ExerciseAnswerOption, ExerciseReport

from core.serializers import StringPrimaryKeyRelatedField
from theory.models import Topic


class ExerciseSerializer(serializers.ModelSerializer):
    topic = StringPrimaryKeyRelatedField(queryset=Topic)
    options = StringPrimaryKeyRelatedField(queryset=ExerciseAnswerOption, many=True)

    class Meta:
        model = Exercise
        fields = ('id', 'title', 'description', 'topic', 'options')


class ExerciseReportSerializer(serializers.ModelSerializer):
    exercise = StringPrimaryKeyRelatedField(read_only=True)
    exercise_id = serializers.IntegerField(write_only=True)

    option = StringPrimaryKeyRelatedField(read_only=True)
    option_id = serializers.IntegerField(write_only=True)

    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'exercise', 'option', 'is_correct', 'exercise_id', 'option_id')

    def create(self, validated_data):
        option = ExerciseAnswerOption.objects.get(pk=validated_data.pop('option_id'))
        exercise = Exercise.objects.get(pk=validated_data.pop('exercise_id'))

        if option and exercise:
            report = ExerciseReport.objects.create(answer=option, exercise=exercise)
            report.save()

            return report

        if not option:
            raise serializers.ValidationError('Вариант ответа не найден')
        if not exercise:
            raise serializers.ValidationError('Задание не найдено')

