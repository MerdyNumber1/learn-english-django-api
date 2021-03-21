from rest_framework import serializers

from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Exercise
        fields = ('title', 'description', 'correct_option')
