from rest_framework import serializers

from .models import Topic, Article


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')

