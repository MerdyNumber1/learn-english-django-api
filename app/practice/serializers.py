from rest_framework import serializers

from .models import Exercise, ExerciseAnswerOption, ExerciseReport

from theory.serializers import TopicSerializer
from profile.serializers import UserSerializer


class ExerciseOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseAnswerOption
        fields = ('id', 'option')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'title', 'description')


class ExerciseReportCreationSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())
    answer = serializers.PrimaryKeyRelatedField(queryset=ExerciseAnswerOption.objects.all())

    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'exercise', 'answer', 'is_correct')

    def create(self, validated_data):
        report = ExerciseReport.objects.create(
            answer=validated_data['answer'],
            exercise=validated_data['exercise'],
            user=self.context['request'].user
        )
        report.save()

        return report


class ExerciseReportDetailSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer()
    answer = ExerciseOptionSerializer()
    user = UserSerializer()

    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'exercise', 'answer', 'is_correct', 'user')


class ExerciseReportSerializer(serializers.ModelSerializer):
    answer = ExerciseOptionSerializer()
    is_correct = serializers.ReadOnlyField()

    class Meta:
        model = ExerciseReport
        fields = ('id', 'answer', 'is_correct')


class ExerciseDetailSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    options = ExerciseOptionSerializer(many=True)
    report = serializers.SerializerMethodField()
    correct_option = serializers.SerializerMethodField()

    def get_report(self, exercise):
        report = ExerciseReport.objects\
            .filter(user__id=self.context['request'].user.id, exercise__id=exercise.id)\
            .first()

        if report:
            return ExerciseReportSerializer(report).data

        return None

    def get_correct_option(self, exercise):
        if self.get_report(exercise):
            return ExerciseOptionSerializer(exercise.correct_option).data

        return None

    class Meta:
        model = Exercise
        fields = ('id', 'title', 'description', 'topic', 'options', 'report', 'correct_option')
