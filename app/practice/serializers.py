from rest_framework import serializers

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

    user = StringPrimaryKeyRelatedField(read_only=True)

    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'exercise', 'option', 'is_correct', 'exercise_id', 'option_id', 'user', 'user_id')

    def create(self, validated_data) -> ExerciseReport:
        try:
            ExerciseReport.objects.get(user__id=self.context['request'].user.id)
            raise serializers.ValidationError({'detail': 'Ответ на задание уже существует'})
        except ExerciseReport.DoesNotExist:
            pass

        try:
            option = ExerciseAnswerOption.objects.get(pk=validated_data.pop('option_id'))
        except ExerciseAnswerOption.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Вариант ответа не найден'})

        try:
            exercise = Exercise.objects.get(pk=validated_data.pop('exercise_id'))
        except Exercise.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Задание не найдено'})

        report = ExerciseReport.objects.create(
            answer=option,
            exercise=exercise,
            user=self.context['request'].user
        )
        report.save()

        return report
