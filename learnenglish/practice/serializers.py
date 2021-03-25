from rest_framework import serializers

from .models import Exercise

from core.serializers import StringPrimaryKeyRelatedField
from theory.models import Topic


class ExerciseSerializer(serializers.ModelSerializer):
    topic = StringPrimaryKeyRelatedField(queryset=Topic)

    class Meta:
        model = Exercise
        fields = ('title', 'description', 'topic')
