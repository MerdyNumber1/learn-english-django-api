from rest_framework import serializers

from .models import Topic, Article


class ArticleListingField(serializers.RelatedField):
    queryset = Article

    def to_representation(self, value):
        return {'id': value.id, 'title': value.title}


class TopicListingField(serializers.RelatedField):
    queryset = Topic

    def to_representation(self, value):
        return {'id': value.id, 'title': value.title}


class TopicSerializer(serializers.ModelSerializer):
    articles = ArticleListingField(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'description', 'articles')


class ArticleSerializer(serializers.ModelSerializer):
    topic = TopicListingField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'topic')

