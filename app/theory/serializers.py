from rest_framework import serializers

from .models import Topic, Article

from practice.models import Exercise


class TopicExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'title')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title')


class TopicDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)
    exercises = TopicExerciseSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'description', 'articles', 'exercises',)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'description')


class ArticleDetailSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topic')

