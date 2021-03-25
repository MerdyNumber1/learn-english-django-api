from rest_framework import serializers

from .models import Topic, Article

from core.serializers import StringPrimaryKeyRelatedField
from practice.models import Exercise


class TopicSerializer(serializers.ModelSerializer):
    articles = StringPrimaryKeyRelatedField(queryset=Article, many=True)
    exercises = StringPrimaryKeyRelatedField(queryset=Exercise, many=True)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'description', 'articles', 'exercises')


class ArticleSerializer(serializers.ModelSerializer):
    topic = StringPrimaryKeyRelatedField(queryset=Topic)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topic')

