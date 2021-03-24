from rest_framework import viewsets
from rest_framework import permissions

from .models import Topic, Article
from .serializers import TopicSerializer, ArticleSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permissions_classes = [permissions.IsAuthenticated]


