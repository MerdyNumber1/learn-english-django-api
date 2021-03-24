from rest_framework import serializers

from .models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'correct_option')


class ExerciseListingField(serializers.RelatedField):
    queryset = Exercise

    def to_representation(self, value):
        return {'id': value.id, 'title': value.title}
