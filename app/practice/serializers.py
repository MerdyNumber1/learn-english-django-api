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
    exercise = StringPrimaryKeyRelatedField(queryset=Exercise)
    option = StringPrimaryKeyRelatedField(queryset=ExerciseAnswerOption)
    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'exercise', 'option', 'is_correct')
