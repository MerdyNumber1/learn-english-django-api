from rest_framework import serializers

from .models import Message
from .services import create_message

from theory.models import Article
from practice.models import Exercise


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), required=False)
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all(), required=False)

    class Meta:
        model = Message
        fields = ('id', 'message', 'type', 'created_at', 'user', 'article', 'exercise')
        read_only_fields = ('id', 'created_at', 'user')

    def create(self, validated_data):
        return create_message(validated_data, self.context['request'].user)


