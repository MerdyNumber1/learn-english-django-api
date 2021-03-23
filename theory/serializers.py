from rest_framework import serializers

from .models import Topic, Article


class TopicSerializer(serializers.ModelSerializer):
    articles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'description', 'articles')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

